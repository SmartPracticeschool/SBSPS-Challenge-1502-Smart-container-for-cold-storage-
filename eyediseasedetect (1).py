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
           if (b=="cataracts" and c>=0.62):
             print("\nEye Disease found is cataracts.\n\nsymptoms of cataracts:\nYou might not have any symptoms at first, when cataracts are mild. But as cataracts grow, they can cause changes in your vision.\nyou may notice that:\n1. Your vision is cloudy or blurry\n2. Colors look faded\n3. You can’t see well at night\n4. Lamps, sunlight, or headlights seem too bright\n5. You see a halo around lights\n6. You see double (this sometimes goes away as the cataract gets bigger)\n7. You have to change the prescription for your glasses often\n\npreventions:\nYou can take steps to protect your eyes and delay cataracts.\n1. Wear sunglasses and a hat with a brim to block the sun.\n2. Quit smoking. If you’re ready to quit, call 1-800-QUIT-NOW (1-800-784-8669) for free support.\n3. Eat healthy. Eat plenty of fruits and vegetables — especially dark, leafy greens like spinach, kale, and collard greens.\n4. Get a dilated eye exam. If you’re age 60 or older, get a dilated eye exam at least once every 2 years.")
           elif (b=="glaucoma" and c>=0.62):
               print ("\nEye Disease found is Glaucoma.\n\nSymptoms of Glaucoma:\nThe signs and symptoms of glaucoma vary depending on the type and stage of your condition.\nOpen-angle glaucoma:\n1. Patchy blind spots in your side (peripheral) or central vision, frequently in both eyes.\n2. Tunnel vision in the advanced stages.\nAcute angle-closure glaucoma\n1. Severe headache\n2. Eye pain\n3. Nausea and vomiting\n3. Blurred vision\n4. Halos around lights\n5. Eye redness\n\nPreventions:\nEarly detection and careful, lifelong treatment can maintain vision in most people. In general, a check for glaucoma should be done:\n1. before age 40, every two to four years\n2. from age 40 to age 54, every one to three years\n3. from age 55 to 64, every one to two years\n4. after age 65, every six to 12 months.\nAnyone with high risk factors should be tested every year or two after age 35. Those at higher risk include people of African descent, people with diabetes, and people with a family history of glaucoma. You are at increased risk if you have a parent or brother or sister with glaucoma.")
           else:
             print ('NO Eye Disease found')
    except:
         print("Not found")
           
