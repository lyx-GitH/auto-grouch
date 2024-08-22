import sys
from courses import Course, CourseList
from datetime import datetime
import time

if len(sys.argv) < 3:
    print("Could not run Grouch; include the desired upcoming term (Fall, Spring, Summer) and use at least one CRN")
    sys.exit(1)

season = sys.argv[1]
now = datetime.now()
term = ''

if season.lower() == 'spring':
    term = f'{now.year + 1}' + '02' if now.month > 4 else f'{now.year}' + '02'
else:
    term = f'{now.year}' + '05' if season.lower() == 'summer' else f'{now.year}' + '08'

crns = sys.argv[2:]

while True:
    courses = [Course(crn, term) for crn in crns] # use soup to refresh course info, so fetch every time

    lst = CourseList(courses)
    # lst.run_notifiers()
    lst.submit_avail_course()
    time.sleep(2) # can change the inerval here
    
