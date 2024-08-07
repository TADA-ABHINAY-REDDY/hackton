from deep_sort_realtime.deepsort_tracker import DeepSort

class DeepSortTracker:
    def __init__(self, max_age=30):
        self.deepsort = DeepSort(max_age=max_age)

    def update(self, detections, frame):
        return self.deepsort.update_tracks(detections, frame=frame)
