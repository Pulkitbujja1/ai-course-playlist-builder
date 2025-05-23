# Define a Lesson node for the Linked List
class Lesson:
    def __init__(self, title, duration, difficulty):
        self.title = title
        self.duration = duration
        self.difficulty = difficulty
        self.next = None

# Define the Linked List to manage the course
class CoursePlaylist:
    def __init__(self):    # constructor 
        self.head = None
# method for add a lesson
    def add_lesson(self, title, duration, difficulty):
        new_lesson = Lesson(title, duration, difficulty)
        if self.head == None:    #First Node
            self.head = new_lesson
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = new_lesson
        print(f"Lesson '{title}' added successfully!")   #(f"" is used to put vaiable in string )

# method for view a all lesson
    def view_lesson(self):
        if self.head == None:
            print("no lesson available")
            return
        current = self.head
        index = 1
        print("\nCourse Lessons:")
        while current != None:
            print(f"{index}.{current.title} ({current.duration}mins,{current.difficulty})")
            current = current.next
            index += 1

#  method for remove a lesson
    def remove_lesson(self,title):
        if self.head == None:
            print("no lessons to remove")
            return

        if self.head.title.lower() == title.lower() :    # lower() method is used to convert all the characters in a string to lowercase
            self.head = self.head.next
            print(f"removed lesson: {title}")
        
        current = self.head
        while current.next != None:
            if current.next.title.lower() == title.lower() :
                current.next = current.next.next
                print(f"removed lesson:{title}")
                return
            current = current.next

        print(f"lesson titled '{title}' not found")

# method for to get a next lesson it means it will give a next lesson to complete it
    def get_next_lesson(self,completed_title):
        current = self.head 
        while current :
            if current.title not in completed_title:  #(not in) it will check absence 
                print(f"you next lesson is - {current.title} ({current.duration},{current.difficulty})")
                return
            current = current.next
        print("you have completed all lesson")

completed_lessons= []   # Array to track completed lessons

course = CoursePlaylist()

# menu
def main():
    while True:     #We want a loop that runs forever,
        print("\n--  AI Course Playlist Menu --")
        print("1. add_lesson")
        print("2. view_lesson")
        print("3. completed_lesson")
        print("4. get_next_lesson")
        print("5. remove_lesson ")
        print("6. exit")
        choice = input("select the number : ")

        if choice == "1": 
            title = input("Enter lesson title: ")
            duration = input("Enter duration (in minutes): ")
            difficulty = input("Enter difficulty (easy/medium/hard): ")
            course.add_lesson(title,duration,difficulty)
        
        elif choice == "2":
           course.view_lesson()

        elif choice == "3":
            title = input("Enter the lesson title to mark as completed: ")
            completed_lessons.append(title)
            print(f"Marked '{title}' as completed.")

        elif choice == "4":
            course.get_next_lesson(completed_lessons)

        elif choice == "5":
            title = input("Enter the title of the lesson to remove: ")
            course.remove_lesson(title)
        elif choice == "6":
            print("GOOD BYE")
            break

        else: 
            print("Invalid choice. Please try again.")

main()    #run this program



        
        