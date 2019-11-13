import cv2

def  same_output_window():
    color_puppies = cv2.imread('puppies.jpg')
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('output', (600,600))
    cv2.imshow('output', color_puppies)  
    cv2.waitKey(0)

    blackandwhite_puppies = cv2.cvtColor(color_puppies, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("output", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('output', (600,600))
    cv2.imshow('output', blackandwhite_puppies)  
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    
def different_output_windows():
    color_puppies = cv2.imread('puppies.jpg')
    cv2.namedWindow("color", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('color', (600,600))
    cv2.imshow('color', color_puppies)  

    blackandwhite_puppies = cv2.cvtColor(color_puppies, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow("blackandwhite", cv2.WINDOW_NORMAL)
    cv2.resizeWindow('blackandwhite', (600,600))
    cv2.imshow('blackandwhite', blackandwhite_puppies)  
    cv2.waitKey(0)

    cv2.destroyAllWindows()
    
same_output_window()
different_output_windows()