def vp():
    secret = "topsecret"
    got = input("Enter password ")
    
    while got != secret:
       got = input("Enter password ")
       
    print ("Success")
    return True
        

