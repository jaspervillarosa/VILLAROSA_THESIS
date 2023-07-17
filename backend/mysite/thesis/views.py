from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core.files.storage import FileSystemStorage
from keras.models import load_model
from keras.preprocessing import image
import json
from tensorflow import Graph
import tensorflow as tf
import numpy as np
import os
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()


# img_height, img_width = 224,224
# with open('./models/imagenet_classes.json', 'r') as f:
#     labelInfo = f.read()

# labelInfo = json.loads(labelInfo)
model = load_model('./models/MobileNetV2_Architecture_coconutDamages_ai_training.h5')


# model_graph = Graph()
# with model_graph.as_default():
#     tf_Session = tf.compat.v1.Session()
#     with tf_Session.as_default():
#         model=load_model('./models/MobileNetV2_Architecture_coconutDiseases_ai_training.h5')
# def index(request):
#     return HttpResponse("Hello World!")

from keras.applications import MobileNetV2
# The line of code initializes a ResNet50 convolutional base model with pre-trained weights from ImageNet, excluding the top (classification) layer, and setting the input shape to (150, 150, 3).  
conv_base = MobileNetV2(weights='imagenet',
                  include_top=False)

def index(request):
    context={'a': 1}
    print("Hello World")
    return render(request, 'index.html', context)

# Create your views here.

def predictImage(request):
    print("Hello Jasper")
    print("This is the request:", request)
    print("This is the WSGI:", request.POST.dict())
    print("This is the fileName:", request.FILES['filePath'])

    fileObj = request.FILES['filePath']
    fs=FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj) 
    filePathName= fs.url(filePathName)
    print("Saved successfully!")

    testimage = '.'+filePathName
    img = image.load_img(testimage, target_size=(150, 150))
    test_image_array = image.img_to_array(img)
    test_image_array = np.expand_dims(test_image_array, axis=0)
    test_image_array=test_image_array/225 # Normalize the pixel values (optional)
    features_batch = conv_base.predict(test_image_array)
    test_image_array = np.reshape(features_batch, (1, 4 * 4 * 1280))
    predi = model.predict(test_image_array)
    
    
    score = float(predi[0])
    scaleInsectDamageScore = round(100 * score)
    rhinocerosBeetleDamageScore = round(100 * (1 - score))

    result = f"This image is {rhinocerosBeetleDamageScore}% Coconut Rhinoceros Beetle Damage and {scaleInsectDamageScore}% Coconut Scale Insect Damage."

    if scaleInsectDamageScore > rhinocerosBeetleDamageScore:
        identification = "Diagnosis: Coconut Scale Insect Damage"
        solution = "Management Strategies \n\n Cultural Method:Regulated prunning of infested fronds \n Chemical Method: Chemical control using systemic insecticides, FPA prescribed for coconut pests by trunk injection(for emergency only)\n. Topical application of vegetable oil in young palms can be done during cooler months \n Biological Method: Sustained release of biological control agents like Chilochorus sp., Telsimia sp., Pseudoscymnus anomalus, Cybocephalus sp., Bathracedra sp., Comperiella calauanica\n Regulatory Control: Implementation of quarantine regulations and establishment of checkpoints (PCA Davao Research Center, 2023)"
    elif scaleInsectDamageScore < rhinocerosBeetleDamageScore:
        identification = "Diagnosis: Coconut Rhinoceros Beetle Damage"
        solution = "Management Strategies \n\n Biological Control: Establishment of coconut log traps inoculated with Green Muscardine Fungus (GMF) granules. Concentrated Oryctes nudivurus is dropped to the mouth of beetles. Infection spreads through mating and visit in breeding sites \n Cultural Control: Collection and utilization of coconut debris or farm waste t avoid piling. PRactice farm sanitation. Regular inspection of all possible breeding sites and collection of all stages of the beetle. Plant covercrops if intercropping is not practiced \n Chemical Control: Installation of rhinoceros beetle pheromone in traps, enhanced with food bait (PCA Davao Research Center, 2023)"
    else:
        identification = "Diagnosis: Record of this data does not exist!"
        solution = "Not applicable"

    # predictedLabel = labelInfo[str(np.argmax(predi[0]))]

    contexttwo={'filePathName': filePathName, 'result': result, 'identification': identification, 'solution': solution}

    return render(request, 'index.html', contexttwo)

def viewDatabase(request):
    listofImages = os.listdir('./media/')
    listofImagePath = ['./media/'+i for i in listofImages]
    fs=FileSystemStorage()
    context = {'listofImagePath': listofImagePath}
    return render(request, 'viewDB.html', context)

def captureImage(request):
    context = {}
    return render(request, 'captureMedia.html', context)