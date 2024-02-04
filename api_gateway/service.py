# api_gateway/service.py
class DataService:
    data_dict = {}

    @classmethod
    def add_data(cls, data_id, data_text):
        print("data_id:" , data_id, "\ndata_test:", data_text)
        cls.data_dict[data_id] = data_text

    @classmethod
    def get_all_data(cls):
        print("but is this happening though")
        return cls.data_dict
