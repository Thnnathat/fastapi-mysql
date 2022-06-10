from connector import Get, Post
conn1 = Get()
conn2 = Post() 
    
class Activity:
    def update_hw(self, Id, status, value):
        boolean = conn1.update_hw(Id, status, value)
        if boolean:
            data = {"error": False}
        else:
            data = {"error": True}
        return data

    def update_post(self, Id, name, Type):
        boolean = conn2.update_post(Id, name, Type)
        if boolean:
            data = {"error": False}
        else:
            data = {"error": True}
        return data
        