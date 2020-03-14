class FrameVehicleCo2:
    """
        FrameVehicleCo2(frame_id=int, contour_id=int, vehicle_type=string, emission=float)

            Object containing the calculated data of a vehicle.

            Parameters
            ----------
            frame_id : int
                Id of the frame
            contour_id : int
                Id of the bounding box
            type_vehicle : String
                Detected vehicle type/model
            emission : float
                CO2 emission output of the vehicle in gram
        """

    def __init__(self, frame_id, contour_id, type_vehicle, emission):
        self.frame_id = frame_id
        self.contour_id = contour_id
        self.type_vehicle = type_vehicle
        self.emission = emission
