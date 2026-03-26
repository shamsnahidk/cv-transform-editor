import cv2
from transformations import translate, rotate, scale, shear

image = cv2.imread("assets/sample.jpg")

while True:
    print("\nChoose Transformation:")
    print("1. Translate")
    print("2. Rotate")
    print("3. Scale")
    print("4. Shear")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        tx = int(input("Enter x shift: "))
        ty = int(input("Enter y shift: "))
        result = translate(image, tx, ty)

    elif choice == "2":
        angle = float(input("Enter angle: "))
        result = rotate(image, angle)

    elif choice == "3":
        fx = float(input("Scale x: "))
        fy = float(input("Scale y: "))
        result = scale(image, fx, fy)

    elif choice == "4":
        shx = float(input("Shear x: "))
        shy = float(input("Shear y: "))
        result = shear(image, shx, shy)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
        continue

    cv2.imshow("Transformed Image", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
