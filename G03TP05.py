#QR CODE GENERATOR
while True:

    import qrcode as qr
    inp=input("ENTER THE URL TO GENERTAE THE QR CODE: ")
    img=qr.make(inp)
    saved_name=input("ENTER THE NAME WITH WHICH YOU WANT TO SAVE YOUR QR CODE (CANNOT BE SAME AS A PRE-EXISTING FILE): ")
    if not saved_name.lower().endswith('.png'):
        saved_name += '.png'
    img.save(saved_name)
    print(f"THE QR CODE HAS BEEN GENERATED AND SAVED IN YOUR PYTHON FOLDER AS {saved_name}")


