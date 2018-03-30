# https://stackoverflow.com/questions/1883980/find-the-nth-occurrence-of-substring-in-a-string
def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

file_to_be_read = input("Which file do you want to open? (Please specify the full filename.)\n")

rtz_file = open(file_to_be_read, 'r')

file_to_be_written = input("Which file do you want to write to? (The file ending 'rtz' will be added automagically.)\n")

file = open(file_to_be_written + ".rtz", "w")

count = 0

schedule_count = 0

date = "2018-04-06"

hours = 10

minutes = 40

seconds = 11

for line in rtz_file:
    line = line.strip()
    if line:
        if "<!--" in line:
            pass
        else:
            if line.startswith('<waypoint id="'):
                count += 1
                file.write(line[:14] + str(count) + line[find_nth(line, '"', 2):] + '\n')
                # file.write(line[:14] + str(count) + line[find_nth(line, '"', 2):])
            if "</waypoint><waypoint" in line:
                count += 1
                file.write(line[0:11] + '\n' + line[11:25] + str(count) + line[find_nth(line, '"', 2):] + '\n')
                # file.write(line[0:11] + '\n' + line[11:25] + str(count) + line[find_nth(line, '"', 2):])
            else:
                if "<waypoint id=" in line:
                    pass
                else:
                    if "<scheduleElement eta=" in line:
                        pass
                    else:
                        file.write(line + '\n')
                    if "<calculated" in line:
                        for number in range(count):
                            schedule_count += 1
                            seconds += 13
                            if seconds < 45:
                                seconds += 14
                            elif seconds > 59:
                                seconds = 15
                            if minutes < 59:
                                minutes += 1
                            elif minutes == 59:
                                minutes = 0
                                hours += 1
                            if minutes < 9:
                                file.write('<scheduleElement eta="' + date + "T" + str(hours) + ":0" + str(minutes) + ":" + str(seconds) + '.000Z"' + ' speed="12.00' + '"' + ' waypointId="' + str(schedule_count) + '"/>' + '\n')
                            elif minutes >= 10:
                                file.write('<scheduleElement eta="' + date + "T" + str(hours) + ":" + str(minutes) + ":" + str(seconds) + '.000Z"' + ' speed="12.00' + '"' + ' waypointId="' + str(schedule_count) + '"/>' + '\n')
                    # file.write(line + '\n')
