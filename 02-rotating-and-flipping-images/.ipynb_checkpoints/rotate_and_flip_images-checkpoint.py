# Import library
import cv2

# Load default image
puppies = cv2.imread('puppies2.png')

def rotate(x):    
    """
    rotate() function takes a parameter x (integer value) and outputs a window with default image
    
    if x = 1:
    default image will be rotated 90 degrees clockwise
    
    if x = 2:
    default image will be rotated 90 degress counter-clockwise
    
    if x = 3:
    default image will be rotated 180 degrees
    """
    try:
        if int(x) == 1:
            puppies_rotated = cv2.rotate(puppies, cv2.ROTATE_90_CLOCKWISE)
        elif int(x) == 2:
            puppies_rotated = cv2.rotate(puppies, cv2.ROTATE_90_COUNTERCLOCKWISE)
        elif int(x) == 3:
            puppies_rotated = cv2.rotate(puppies, cv2.ROTATE_180)
        else:
            print("Sorry invalid option")       
            
        cv2.namedWindow('rotateoutput', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('rotateoutput', (600,600))
        cv2.imshow('rotateoutput', puppies_rotated)  
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print("Sorry invalid option")

def flip(y):    
    """
    flip() function takes a parameter y (integer value) and outputs a window with default image
    
    if y = 1:
    default image will be flipped vertcially or upside down (i.e., flipCode = 0)
    
    if y = 2:
    default image will be flipped horizontally with flipCode > 0 (i.e., flipCode = 1)
    
    if y = 3:
    default image will be flipped image vertically and horizontally, meaning image is first flipped vertically (upside down), then flipped horizontally (left to right) with flipCode < 0 (i.e., flipCode = -1)
    """
    try:
        if int(y) == 1:
            puppies_rotated = cv2.flip(src=puppies, flipCode=0)
        elif int(y) == 2:
            puppies_rotated = cv2.flip(src=puppies, flipCode=1)
        elif int(y) == 3:
            puppies_rotated = cv2.flip(src=puppies, flipCode=-1)
        else:
            print("Sorry invalid option")        
        
        cv2.namedWindow('flipoutput', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('flipoutput', (600,600))
        cv2.imshow('flipoutput', puppies_rotated)  
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except:
        print("Sorry invalid option")
        
rotate(1)
flip(1)