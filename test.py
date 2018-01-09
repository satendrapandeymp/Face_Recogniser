import face_recognition, os

names = os.listdir('train')

people_name = []
encodes = []

for name in names:
    temp_name = name[:-4]
    people_name.append(temp_name)
    if not os.path.exists(temp_name):
        os.mkdir(temp_name)
    name = "train/" + name
    temp_img = face_recognition.load_image_file(name)
    encode = face_recognition.face_encodings(temp_img)[0]
    encodes.append(encode)

def result(unknown_encoding,abspath, filename, image):
    tolerance = .5
    count = 1
    check = False

    faces_bboxes = face_recognition.face_locations(image)
    if len(faces_bboxes) != 1:
        print 'an image without a guy or more than 1 guy'
        return 1

    while (not check):

        print 'iteration no ', count, 'tolerance is ', tolerance
        count += 1

        for i in range(len(encodes)):
            check = face_recognition.compare_faces([encodes[i]], unknown_encoding, tolerance )[0]
            print check , people_name[i]
            if check:
                os.rename(abspath, people_name[i] + '/' + filename )
                print "Guy Identifies as - ", people_name[i]
                break

        tolerance += .02
    return 0

testnames = os.listdir('test')

for name in testnames:
    loc = "test/" + name
    temp_img = face_recognition.load_image_file(loc)
    encode = face_recognition.face_encodings(temp_img)[0]
    result(encode, loc, name, temp_img)
