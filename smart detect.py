import json
from ibm_watson import VisualRecognitionV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('OsvxlNvqndnd4R1IQeuh-0xaMkPH_sf_KYUrnFobo0FI')
visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    authenticator=authenticator
)



with open('./test1.jpg', 'rb') as images_file:
    classes = visual_recognition.classify(
        images_file=images_file,
        threshold='0.6',
        owners=["me"]).get_result()
    a=json.dumps(classes, indent=2)
    #print (a);
    a=a.split('\n')
    count=0
    b=''
    c=''
    try:
        for i in a:
         count+=1
         if(count==10):
           b=i.split(": ")
           b=b[1]
           b=b[1:-2]
           #print (b)
         if (count==11):
           #print (i)
           c=i.split(": ")
           c=float(c[1])
           if (b=="Good Apple" and c>=0.62):
             print("\nFound Good Apple")
           elif (b=="Bad Apple" and c>=0.62):
              print ("\nFound Bad Apple")
           else:
             print ('NO found')
    except:
         print("Not found")
           
