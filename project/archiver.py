def archiver(file_list):
    arr = bytearray()

    for filename in file_list:
        current_path = 'files/' + filename
        with open(current_path, "rb") as file:
            contents = file.read()

        arr.extend(bytearray((toHex(len(filename), 2) + filename + toHex(len(contents), 10)).encode() + contents))

    with open('archive.txt', 'wb') as archive:
        archive.write(arr)
    return arr

def toHex(name_or_contents, digits: int):
    result = hex(name_or_contents)
    while len(result) != 2 + digits:
        result = result[:2] + '0' + result[2:]
    return result

def unarchiver(archive):
    with open(archive, 'rb') as archived_file:
        contents = archived_file.read()
        finish_line = len(contents)
        progress = 0

        while progress < finish_line:
            begin_point = progress
            progress += 4
            name_length = int((contents[begin_point:progress].decode()), 16)

            begin_point = progress
            progress += name_length
            filename = contents[begin_point:progress].decode()

            with open(filename, 'wb') as current_file:
                begin_point = progress
                progress += 12
                file_length = int((contents[begin_point:progress].decode()), 16)

                begin_point = progress
                progress += file_length
                file_data = contents[begin_point:progress]
                current_file.write(file_data)

    return 0

files = archiver("test1.txt", "test2.txt", "test3.txt")
unarchiver("archive.txt.")
