def dict_to_object(data):
    class CustomObject:
        pass

    custom_object = CustomObject()

    for key, value in data.items():
        setattr(custom_object, key, value)

    return custom_object
