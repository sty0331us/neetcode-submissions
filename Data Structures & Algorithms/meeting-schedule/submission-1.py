"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x: x.start)
        
        for i in range(1, len(intervals)):
            prev_meeting = intervals[i-1]
            cur_meeting = intervals[i]

            if prev_meeting.end > cur_meeting.start:
                return False
        
        return True

