class Contour:
    """
        Contour(contour_id=int, pos=int, vehicle_type=string, frame_id=int)

            Object representing the bounding box of a detected vehicle from an image.

            Parameters
            ----------
            contour_id : int
                Id of the bounding box
            pos : tuple of 4 ints (x1, y1, x2, y2)
                Coordinate of the two points defining the bounding box
            vehicle_type : string
                Type of vehicle (car, truck, bus, motorcycle...)
            frame_id : int
                Id of the frame
        """
    def __init__(self, contour_id, pos, vehicle_type, frame_id):
        self.contour_id = contour_id
        self.pos = pos
        self.vehicle_type = vehicle_type
        self.frame_id = frame_id

    def get_pos(self):
        return self.pos[0], self.pos[1], self.pos[2], self.pos[3]

    def get_vehicle_id(self):
        return self.contour_id

    def get_vehicle_type(self):
        return self.vehicle_type

    def get_id_frame(self):
        return self.frame_id
