import pymysql as lite
from configparserpy import getcreds

# Functionality part goes here
class DatabaseManage:
    def __init__(self):

        global conn
        try:
            # creddetails = getcreds()
            # conn = lite.connect(
            #     host="localhost", user="root", password="root", database="demodb"
            # )

            creddetails = getcreds()
            conn = lite.connect(**creddetails)

            with conn:
                cur = conn.cursor()
                sql = """create table if not exists course(
                    id int not null auto_increment,
                    name varchar(255) not null, description text, price varchar(255) not null,
                    is_private boolean not null default 1, primary key(id))
                """
                cur.execute(sql)

        except Exception as e:
            print(e)
            print("Unable to create a db!")

    def insert_data(self, data):
        try:
            with conn:
                cur = conn.cursor()
                sql = "insert into course (name,description,price,is_private) values (%s,%s,%s,%s)"
                cur.execute(sql, data)
                return True
        except Exception:
            print("OOPs something goes wrong")
            return False

    def fetch_data(self):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("select * from course")
                return cur.fetchall()
        except Exception:
            print("OOPs something goes wrong!")
            return False

    def delete_data(self, id):
        try:
            with conn:
                cur = conn.cursor()
                cur.execute("delete from course where id = %s", (id,))
                return True
        except Exception:
            print("OOps something goes wrong!")
            return False


# Presentation part goes here
def main():

    while True:
        print("*" * 40)
        print("\n :: COURSE MANAGEMENT SYSTEM :: \n")
        print("*" * 40)

        db = DatabaseManage()

        print("#" * 40)
        print("\n :: USER MANUAL :: \n")
        print("#" * 40)

        print("\n Press 1. Insert a new course: \n")
        print(" Press 2. Show all courses: \n")
        print("Press 3. Delete a course (Need id of course): \n")
        print("Press 4. Exit \n")
        print("#" * 40)

        choice = input("\n Enter a choice: \n")

        if choice == "1":
            name = input("\n Enter course name: \n")
            description = input("Enter course description: \n")
            price = input("Enter course price: \n")
            is_private = input("Is the course private(0/1): ")

            if db.insert_data([name, description, price, is_private]):
                print("Course inserted successfully")
                continue
            else:
                print("OOPs something went wrong!")

        elif choice == "2":

            print("\n :: Course List :: \n")

            for index, item in enumerate(db.fetch_data()):
                print("\n Course Id : " + str(item[0]))
                print("Course Name : " + item[1])
                print("Course Description : " + item[2])
                print("Course Price : " + item[3])
                private = "YES" if int(item[4]) else "NO"
                print("Is private :" + private)

            break

        elif choice == "3":

            record_choice = input("\n Enter id of course : ")

            if db.delete_data(record_choice):
                print("Course deleted successfully")
                continue
            else:
                print("OOPs something went wrong")

        elif choice == "4":

            print("BYE BYE")
            break

        else:

            print("BAD CHOICE")


if __name__ == "__main__":
    main()
