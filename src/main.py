import cv2
from transformations import translate, rotate, scale, shear
from utils import stack_side_by_side, add_labels


def print_matrix(matrix):
    print("\nTransformation Matrix:")
    print(matrix)


def main():
    image_path = "assets/sample.jpg"
    image = cv2.imread(image_path)

    if image is None:
        print(f"Error: Could not load image from {image_path}")
        return

    while True:
        print("\nChoose Transformation:")
        print("1. Translate")
        print("2. Rotate")
        print("3. Scale")
        print("4. Shear")
        print("5. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            tx = int(input("Enter x shift: "))
            ty = int(input("Enter y shift: "))
            result, matrix = translate(image, tx, ty)

        elif choice == "2":
            angle = float(input("Enter angle in degrees: "))
            result, matrix = rotate(image, angle)

        elif choice == "3":
            fx = float(input("Enter scale factor for x: "))
            fy = float(input("Enter scale factor for y: "))
            result, matrix = scale(image, fx, fy)

        elif choice == "4":
            shx = float(input("Enter shear factor for x: "))
            shy = float(input("Enter shear factor for y: "))
            result, matrix = shear(image, shx, shy)

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")
            continue

        print_matrix(matrix)

        labeled_original, labeled_result = add_labels(image, result)
        comparison = stack_side_by_side(labeled_original, labeled_result)

        cv2.imshow("CV Transform Editor", comparison)
        key = cv2.waitKey(0)
        cv2.destroyAllWindows()

        if key == 27:
            break


if __name__ == "__main__":
    main()
