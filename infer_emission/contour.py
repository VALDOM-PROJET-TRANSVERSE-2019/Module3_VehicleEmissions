import json

from PIL import Image


class Contour:
    """
        Contour(frame_id=int, contour_id=int, pos=int, vehicle_type=string)

            Object representing the bounding box of a detected vehicle from an image.

            Parameters
            ----------
            frame_id : int
                Id of the frame
            contour_id : int
                Id of the bounding box
            pos : tuple of 4 ints (x1, y1, x2, y2)
                Coordinate of the two points defining the bounding box
            vehicle_type : string
                Type of vehicle (car, truck, bus, motorcycle...)
        """

    def __init__(self, frame_id, contour_id, pos, vehicle_type, prob):
        self.frame_id = frame_id
        self.contour_id = contour_id
        self.pos = pos
        self.prob = prob
        self.vehicle_type = vehicle_type

    # crop an img of type Image (from PIL)
    def crop_image(self, image):
        return image.crop(self.pos)

    def get_pos(self):
        return self.pos[0], self.pos[1], self.pos[2], self.pos[3]

    def get_vehicle_id(self):
        return self.contour_id

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_id_frame(self):
        return self.frame_id

    # crop a list of img
    # list_path contain paths of list_contour img
    # return an array of cropped images (to save or to feed NN)
    @staticmethod
    def crop_images(list_contour, list_path):
        list_contour = [list_contour]
        arr_cropped = []
        for i in range(len(list_contour)):
            im = Image.open(list_path[i])
            arr_cropped.append(list_contour[i].crop_image(im))
        return arr_cropped

    """
    :parameter bouding_boxes is a list of paths to json files generated by YOLO
    """

    @staticmethod
    def from_bounding_boxes(bounding_boxes_paths):
        bounding_boxes_paths = list(bounding_boxes_paths)
        contours = []

        for bb_path in bounding_boxes_paths:
            with open(bb_path) as json_file:
                data = json.load(json_file)
                for p in data:
                    pos = p['left'], p['bot'], p['right'], p['top']
                    object = p['object']
                    prob = p['proba']
                    contours.append(Contour(0, 0, pos, object, prob))

        return contours


if __name__ == '__main__':
    paths = ["../data/mocks/bounding_boxes/image46.json", "../data/mocks/bounding_boxes/image34.json"]
    contours = Contour.from_bounding_boxes(paths)

    for contour in contours:
        print(contour)
        print(contour.get_vehicle_type())
