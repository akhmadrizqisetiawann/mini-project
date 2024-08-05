class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


new_q = Question("balbalala", "True")
print(new_q.text)











































# class Dog:
#     species = "Canis familiaris"  # atribut kelas

#     def __init__(self, name, age):
#         self.name = name  # atribut instance
#         self.age = age    # atribut instance

# # Membuat objek Dog
# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Lucy", 4)

# # Mengakses atribut kelas
# print(dog1.name, dog1.age)  # Output: Canis familiaris
# print(dog2.species)  # Output: Canis familiaris
