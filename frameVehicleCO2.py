class FrameVehicleCo2:
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
    def __init__(self, frame_id, contour_id, type_vehicle, emission):
        self.contour_id = contour_id
        self.frame_id = frame_id
        self.type_vehicle = type_vehicle
        self.emission = emission
