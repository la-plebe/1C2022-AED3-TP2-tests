import os
import cv2


def to_threshold_matrix(filename: str, threshold: int = 128):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    return (img > threshold).astype(int)


if __name__ == "__main__":
    for filename in os.listdir("img"):
        name_components, _ = os.path.splitext(filename)
        name, components = name_components.split("_")
        m = to_threshold_matrix(os.path.join("img", filename))

        with open(os.path.join("output", "ej2", f"{name}.in"), "w") as input_file:
            input_file.write(" ".join(map(str, m.shape)) + "\n")
            for row in m:
                input_file.write(" ".join(map(str, row)) + "\n")

        with open(os.path.join("output", "ej2", f"{name}.out"), "w") as output_file:
            output_file.write(str(components))
