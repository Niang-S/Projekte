import cv2
import numpy as np
import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET



def load_and_display_image_blob2_(title, imgLoc1, imgLoc2, z_hbo, z_led2, exposure_hbo, exposure_led2, widthPix, heightPix):
    imgList32_im1 = []
    imgList32_im2 = []
    
    #-----Image 1-------------------------
    with open(imgLoc1, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix1 = int.from_bytes(f4.read(2), "little")
            imgList32_im1.append(pix1)
            count += 1
    #-----Image 2-------------------------
    with open(imgLoc2, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix2 = int.from_bytes(f4.read(2), "little")
            imgList32_im2.append(pix2)
            count += 1
 
    imgNump32_im1 = np.array(imgList32_im1)
    imgNump32_im2 = np.array(imgList32_im2)
   
    imgMat1 = imgNump32_im1.reshape(heightPix, widthPix, 1)
    imgMat2 = imgNump32_im2.reshape(heightPix, widthPix, 1)
    
    img1 = np.uint16(imgMat1)
    img2 = np.uint16(imgMat2)
       
    
    # Check if the image dimensions are valid
    if img1.shape[0] > 0 and img1.shape[1] > 0 and img2.shape[0] > 0 and img2.shape[1] > 0:
        # Display the image
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        #img = clahe.apply(img)
        #cv2.imshow('Image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        # Calculate the histogram
        hist1 = cv2.calcHist([img1], [0], None, [65535], [0, 65535])
        hist2 = cv2.calcHist([img2], [0], None, [65535], [0, 65535])
        max_hist1 = np.max(hist1[0:4090])
        max_hist2 = np.max(hist2[0:4090])

        # Plot the histogram
        plt.figure()
        plt.title(title+" image histogram: HBO vs LED2")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.xlim([0, 4090])
        plt.ylim([0, 3000])
        plt.plot(hist1, label='HBO = '+str(exposure_hbo)+'ms; Z = '+str(z_hbo)+'; Max frequency = '+str(max_hist1), color='blue')
        plt.plot(hist2, label='LED2 = '+str(exposure_led2)+'ms; Z = '+str(z_led2)+'; Max frequency = '+str(max_hist2), color='green')
        plt.grid(True)
        plt.legend()
        #plt.bar(bins[:-1], hist, width=1, color='blue', alpha=0.7)
        plt.show()
    else:
        print("Error: Invalid image or dimensions.")

def load_and_display_image_blob(title, imgLoc1, widthPix, heightPix):
    imgList32_im1 = []
    #imgList32_im2 = []
    
    #-----Image 1-------------------------
    with open(imgLoc1, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix1 = int.from_bytes(f4.read(2), "little")
            imgList32_im1.append(pix1)
            count += 1
    
    imgNump32_im1 = np.array(imgList32_im1)
       
    imgMat1 = imgNump32_im1.reshape(heightPix, widthPix, 1)
        
    img1 = np.uint16(imgMat1)
    
       
    
    # Check if the image dimensions are valid
    if img1.shape[0] > 0 and img1.shape[1] > 0:
        # Display the image
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        #img = clahe.apply(img)
        #cv2.imshow('Image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        # Calculate the histogram
        image_8bit = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
        hist1 = cv2.calcHist([image_8bit], [0], None, [255], [0, 255])
        max_hist1 = np.max(hist1[0:255])
        

        # Plot the histogram
        plt.figure()
        plt.title(title+" image histogram")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.xlim([2, 255])
        plt.ylim([0, 250000])
        plt.plot(hist1, color='blue')
        plt.grid(True)
        plt.legend()
        #plt.bar(bins[:-1], hist, width=1, color='blue', alpha=0.7)
        plt.show()
    else:
        print("Error: Invalid image or dimensions.")


def load_and_display_image_blob2(title, imgLoc1, imgLoc2, z_hbo, z_led1, exposure_hbo, exposure_led1, widthPix, heightPix):
    imgList32_im1 = []
    imgList32_im2 = []
    
    #-----Image 1-------------------------
    with open(imgLoc1, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix1 = int.from_bytes(f4.read(2), "little")
            imgList32_im1.append(pix1)
            count += 1
    #-----Image 2-------------------------
    with open(imgLoc2, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix2 = int.from_bytes(f4.read(2), "little")
            imgList32_im2.append(pix2)
            count += 1
 
    imgNump32_im1 = np.array(imgList32_im1)
    imgNump32_im2 = np.array(imgList32_im2)
   
    imgMat1 = imgNump32_im1.reshape(heightPix, widthPix, 1)
    imgMat2 = imgNump32_im2.reshape(heightPix, widthPix, 1)
    
    img1 = np.uint16(imgMat1)
    img2 = np.uint16(imgMat2)
       
    
    # Check if the image dimensions are valid
    if img1.shape[0] > 0 and img1.shape[1] > 0 and img2.shape[0] > 0 and img2.shape[1] > 0:
        # Display the image
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        #img = clahe.apply(img)
        #cv2.imshow('Image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        # Calculate the histogram
        hist1 = cv2.calcHist([img1], [0], None, [65535], [0, 65535])
        hist2 = cv2.calcHist([img2], [0], None, [65535], [0, 65535])
        max_hist1 = np.max(hist1[0:4090])
        max_hist2 = np.max(hist2[0:4090])

        # Plot the histogram
        plt.figure()
        plt.title(title+" image histogram: HBO vs LED1")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.xlim([0, 4090])
        plt.ylim([0, 3000])
        plt.plot(hist1, label='HBO exposure = '+str(exposure_hbo)+'ms; Z = '+str(z_hbo)+ '; Max frequency = '+str(max_hist1), color='blue')
        plt.plot(hist2, label='LED1 exposure = '+str(exposure_led1)+'ms; Z = '+str(z_led1)+ '; Max frequency = '+str(max_hist2), color='red')
        plt.grid(True)
        plt.legend()
        #plt.bar(bins[:-1], hist, width=1, color='blue', alpha=0.7)
        plt.show()
    else:
        print("Error: Invalid image or dimensions.")


def load_and_display_image_blob3(title, imgLoc1, imgLoc2, imageLoc3, z_hbo, z_led1, z_led2, exposure_hbo, exposure_led1, exposure_led2, widthPix, heightPix):
    imgList32_im1 = []
    imgList32_im2 = []
    imgList32_im3 = []
    #-----Image 1-------------------------
    with open(imgLoc1, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix1 = int.from_bytes(f4.read(2), "little")
            imgList32_im1.append(pix1)
            count += 1
    #-----Image 2-------------------------
    with open(imgLoc2, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix2 = int.from_bytes(f4.read(2), "little")
            imgList32_im2.append(pix2)
            count += 1
    #-----Image 3-------------------------
    with open(imageLoc3, "rb") as f4:
        count = 0
        while count < (widthPix * heightPix):
            pix3 = int.from_bytes(f4.read(2), "little")
            imgList32_im3.append(pix3)
            count += 1

    imgNump32_im1 = np.array(imgList32_im1)
    imgNump32_im2 = np.array(imgList32_im2)
    imgNump32_im3 = np.array(imgList32_im3)

    imgMat1 = imgNump32_im1.reshape(heightPix, widthPix, 1)
    imgMat2 = imgNump32_im2.reshape(heightPix, widthPix, 1)
    imgMat3 = imgNump32_im3.reshape(heightPix, widthPix, 1)

    img1 = np.uint16(imgMat1)
    img2 = np.uint16(imgMat2)
    img3 = np.uint16(imgMat3)
    
    
    # Check if the image dimensions are valid
    if img1.shape[0] > 0 and img1.shape[1] > 0 and img2.shape[0] > 0 and img2.shape[1] and img3.shape[0] > 0 and img3.shape[1] > 0:
        # Display the image
        #clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        #img = clahe.apply(img)
        #cv2.imshow('Image', img)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        # Calculate the histogram
        hist1 = cv2.calcHist([img1], [0], None, [65535], [0, 65535])
        hist2 = cv2.calcHist([img2], [0], None, [65535], [0, 65535])
        hist3 = cv2.calcHist([img3], [0], None, [65535], [0, 65535])

        max_hist1 = np.max(hist1[0:4090])
        max_hist2 = np.max(hist2[0:4090])
        max_hist3 = np.max(hist3[0:4090])

        # Plot the histogram
        plt.figure()
        plt.title(title+" image histogram: HBO vs LED1 vs LED2")
        plt.xlabel("Pixel Value")
        plt.ylabel("Frequency")
        plt.xlim([0, 4090])
        plt.ylim([0, 3000])
        plt.plot(hist1, label='HBO exposure = '+ str(exposure_hbo)+'ms; Z = '+str(z_hbo)+' ; Max frequency = '+str(max_hist1), color='blue')
        plt.plot(hist2, label='LED1 exposure = '+ str(exposure_led1) +'ms; Z = '+str(z_led1)+' ; Max frequency = '+str(max_hist2), color='red')
        plt.plot(hist3, label='LED2 exposure = '+str(exposure_led2)+'ms; Z = '+str(z_led2)+' ; Max frequency = '+str(max_hist3), color='green')
        plt.grid(True)
        plt.legend()
        #plt.bar(bins[:-1], hist, width=1, color='blue', alpha=0.7)
        plt.show()
    else:
        print("Error: Invalid image or dimensions.")

def load_xml_extract_xyzexp_size(path_to_xml):
# Parse the XML file
    tree = ET.parse(path_to_xml)
    root = tree.getroot()

    # Extract values from the <coordinates> element's attributes
    for coordinates in root.findall(".//coordinates"):
        x = coordinates.get("X")
        y = coordinates.get("Y")
        z = coordinates.get("Z")

        # You can convert these values to the appropriate data types if needed
        x = float(x)
        y = float(y)
        z = float(z)

        # Now, you can use these values as needed
        #print(f"x: {x}, y: {y}, z: {z}")

    for capture in root.findall(".//capture"):
        exposure = capture.attrib['exposure']

        exposure = float(exposure)
        #print(f"exp: {exposure}")

    for size in root.findall(".//size"):
        width = size.attrib['width']
        height = size.attrib['height']

        width = int(width)
        height = int(height)
    return width, height #x, y, z, exposure

# Example usage:
# Replace 'imgLoc', 'widthPix', and 'heightPix' with your actual values
im_blob1 = r'C:\Users\Niang\Documents\LED_HBO_DATA\scanjobs\EZKL560112\pos20\hdr\20230822T083020Z_64e4721c0b90b802b4aa31ec.blob32'
#im_blob2 = r'C:\Users\Niang\Documents\LED_HBO_DATA\scanjobs\EZKL560111\pos16\flimages\20230822T075237Z_64e469450b90b802b4aa248f.blob'
#im_blob3 = r'C:\Users\Niang\Documents\LED_HBO_DATA\scanjobs\EZKL560111\pos31\flimages\20230822T075837Z_64e46aad0b90b802b4aa2968.blob'
xml_1 = im_blob1+".xml"
#xml_2 = im_blob2+".xml"
#xml_3 = im_blob3+".xml"
title="EZKL560112\pos20\hdr "

#z_hbo, exposure_hbo, width, height = load_xml_extract_xyzexp_size(xml_1)
#z_led1, exposure_led1, width, height = load_xml_extract_xyzexp_size(xml_2)
#z_led2, exposure_led2, width, height = load_xml_extract_xyzexp_size(xml_3)

width, height = load_xml_extract_xyzexp_size(xml_1)


load_and_display_image_blob(title, im_blob1, width, height)
#load_and_display_image_blob2(title, im_blob1, im_blob2, z_hbo, z_led1, exposure_hbo, exposure_led1, width, height)
#load_and_display_image_blob2_(title, im_blob1, im_blob3, z_hbo, z_led2, exposure_hbo, exposure_led2, width, height)
