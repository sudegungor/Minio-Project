from minio import Minio
from minio.error import S3Error
from PIL import Image



def main():
    # Client oluşturma
    client = Minio(
        "play.min.io",
        access_key="Q3AM3UQ867SPQQA43P2F",
        secret_key="zuf+tfteSlswRu7BJ86wekitnifILbZam1KYY3TG",
    )

    
    found = client.bucket_exists("kelebek")

    if not found:

        #upload image
        client.make_bucket("kelebek")

        client.fput_object(
            "kelebek", "kelebek.jpg", r"C:\\Users\\User\\Pictures\\kelebek.jpg",
        )

        print("Upload done")

    else:
        #Download image
        client.fget_object("kelebek", "kelebek.jpg", r"C:\\Users\\User\\Pictures\\kelebek-2.jpg" )
        print("Bucket 'kelebek' already exists. Download done")


    #resim dosyasını açma
    imageFile = r"C:\\Users\\User\\Pictures\\kelebek-2.jpg"
    imageObj = Image.open(imageFile)

    #resim boyutlarını almak için
    data = imageObj.size
    print ("width(en) %s , height(boy) %s" %(data[0], data[1]))



    #yeni en boy
    width = float(input("En giriniz"))
    height = float(input("Boy giriniz"))


    im2 = imageObj.resize((int(width), int(height)), Image.NEAREST)

    im2.save(r"C:\\Users\\User\\Pictures\\kelebek-yeni.jpg")


    found = client.bucket_exists("kelebek-yeni")

    if not found:

        client.make_bucket("kelebek-yeni")

        client.fput_object(
            "kelebek-yeni", "kelebek-yeni.jpg", r"C:\\Users\\User\\Pictures\\kelebek-yeni.jpg",
        )

        print("Upload done")


    else:
        #Download image        
        print("Bucket 'kelebek-yeni' already exists.")

    
    

if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)