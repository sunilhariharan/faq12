import os


d={'application slowness issue':'download file from this path - http://127.0.0.1:8000/bot/download/ and run and check for avg rsesponse time, if avg response time less than 75 ms, server is down','not able to upload file':'pls install access database engine on ur system',
    'photo not uploading':'size should be less than 512 kb',

    'kyc - app module - application slowness issue':'download file from this path - http://127.0.0.1:8000/bot/download/ and run and check for avg rsesponse time, if avg response time less than 75 ms, server is down','kyc - upload issue - not able to upload file':'pls install access database engine on ur system',
    'kyc - upload issue - photo not uploading':'size should be less than 512 kb',


    'id deleted':'raise a request for id creation',
    'id not available':'id might be dormented',
    'raise a request for id creation':'raise a call log for this with fm support',

    'isac - id related issues - id deleted':'raise a request for id creation',
    'isac - id related issues - id not available':'id might be dormented',
    'isac - id related issues - raise a request for id creation':'raise a call log for this with fm support',


    'procedure for mapping':'raise a call log on isac',
    'showing id dormented':'you will have to create a new id',


    'imap - mapping related module - procedure for mapping':'raise a call log on isac',
       'imap - id related issues - showing id dormented':'you will have to create a new id',


    'iapproval - upload module - cant upload excel file':'delete 2.0 and check again if access database is installed or install it',
    'iapproval - app module - app running slow on ios':'optimisation of code in progress',

    'cant upload excel file':'delete 2.0 and check again if access database is installed or install it',
    'app running slow on ios':'optimisation of code in progress',

    'more money deducted':'not possible,give your contact details,we will get in touch with you',
    'GST for businesses is 18 percent or 28':'28 percent',

    'gst - money related - more money deducted':'not possible,give your contact details,we will get in touch with you',
       'gst - business related - GST for businesses is 18 percent or 28':'28 percent'
}
def fetchResponse(question):
    response = d[question]
    return response


if __name__ == '__main__':
    fetchResponse('who is the president of india')
