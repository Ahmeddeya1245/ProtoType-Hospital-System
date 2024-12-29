def input_valid_int(msg, start=0, end=None):
    while True:
        inp = input(msg)

        if not inp.isdecimal():
            print('Invalid input. Try again!')
        elif start is not None and end is not None:
            if not (start <= int(inp) <= end):
                print('Invalid range. Try again!')
                # another way is to check if int(inp) in range(start, end+1)
            else:
                return int(inp)
        else:
            return int(inp)


class Patient:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    def __str__(self):
        self.status = ['normal', 'urgent', 'super urgent'][self.status]
        return f"{self.name} is {self.status}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.status == other.status


class Hospital:
    def __init__(self, specializations_cnt):
        self.specializations_cnt = specializations_cnt
        self.max_queue = 10
        self.specializations_cnt = [[] for i in range(specializations_cnt)]
        self.normal = 0
        self.urgent = 1
        self.super_urgent = 2

    def can_add_more_patients(self, specializations_cnt):
        for value in self.specializations_cnt[specializations_cnt]:
            if value == 0:
                return "You Cann Add More Patients"
            else:
                return "No more patients can be added"

    def Add_Patient_Smart(self, specialization, name, status):
        spec = self.specializations_cnt[specialization]
        spec.appeed(Patient(name, status))
        spec.sort()

    def add_patient(self, specializaion, name, status):
        spec = self.specializations_cnt[specializaion]
        pat = Patient(name, status)
        if len(spec) > self.max_queue:
            return "no more patient can be Added "
        if status == 0 or len(spec) == 0 :
            spec.append(pat)
        elif status == 1 :
            if spec[-1].status != self.normal :
                spec.append(pat)
            else:
                for idx , patient in enumerate(spec) :
                    if patient.status == self.normal:
                        spec.insert(idx , pat)
                        break
        else :
            if spec[-1].status == self.super_urgent:
                spec.append(pat)
            else:
                for idx , patient in enumerate(spec):
                    if patient.status == self.normal or patient.status==self.urgent:
                        spec.insert(idx,pat)
                        break


    def get_printable_patients_info(self):
        results = []
        for idx, specilization in enumerate(self.specializations_cnt):
            if not specilization:
                continue
            cur_patient = []
            for patient in specilization:
                cur_patient.append(str(patient))
            results.append((idx, cur_patient))
        return results

    def get_next_patients(self, specialization: int):
        if len(self.specializations_cnt[specialization]) == 0:
            return "No patients found"
        else:
            return self.specializations_cnt[specialization].pop(0)

    def remove_patient(self, specialization, name):
        spec = self.specializations_cnt[specialization]
        for idx, patient in enumerate(spec):
            if patient.name == name:
                del spec[idx]
                return True
        return False


class FrontendManager:
    def __init__(self, specializations_cnt=20):
        self.specializations_cnt = specializations_cnt
        self.hospital_manager = Hospital(specializations_cnt)
        self.dummydata()

    def print_menu(self):

        print('\nProgram Options:')
        messages = [
            'Add new patient',
            'Print all patients',
            'Get next patient',
            'Remove a leaving patient',
            'End the program'
        ]
        # let's add the order 1 2 3 4...
        messages = [f'{idx + 1}) {msg}' for idx, msg in enumerate(messages)]
        print('\n'.join(messages))
        msg = f'Enter your choice (from 1 to {len(messages)}): '
        return input_valid_int(msg, 1, len(messages))

    def dummydata(self):
        for i in range(10):
            self.hospital_manager.add_patient(2, 'Dummy' + str(i), i % 3)
        for i in range(4):
            self.hospital_manager.add_patient(5, 'FirstDummy' + str(i), 0)
        for i in range(5):
            self.hospital_manager.add_patient(5, 'SecondDummy' + str(i), 1)
        for i in range(5):
            self.hospital_manager.add_patient(5, 'ThirdDummy' + str(i), 2)
        for i in range(3):
            self.hospital_manager.add_patient(12, 'ForthDummy' + str(i), 2)
        for i in range(3):
            self.hospital_manager.add_patient(13, 'FifthDummy' + str(i), 1)
            self.hospital_manager.add_patient(13, 'FifthDummy' + str(i + 5), 2)

    def run(self):
        while True:
            choice = self.print_menu()
            if choice == 1:
                if not self.hospital_manager.can_add_more_patients():
                    print("No more patients can be added")
                specialization = int(input("Enter specialization: "))
                name = input("Enter patient name: ")
                status = int(input("Enter status(0 normal / 1 urgent / 2 super urgent): "))
                print(self.hospital_manager.add_patient(specialization, name, status))
            elif choice == 2:
                results = self.hospital_manager.get_printable_patients_info()
                if not results:
                    print("No patients found")
                else:
                    for idx, patients_info in results:
                        print(f'Specialization {idx + 1}: There are {len(patients_info)} patients.')
                        print("\n".join(patients_info) + '\n')
            elif choice == 3:
                specialization = int(input("Enter specialization: "))
                patient = self.hospital_manager.get_next_patients(specialization)
                if not patient:
                    print("No Patients , have rest Doctor")
                else:
                    print(f"{patient.name} , please go with doctor")
            elif choice == 4:
                specialization = input_valid_int("Enter specialization: ", 1, self.specializations_cnt) - 1
                name = input("Enter patient name: ")
                ensure = input_valid_int("Are you sure you want to remove a patient from the queue? (1 yes / 0 no): ",
                                         0, 1)

                if self.hospital_manager.remove_patient(specialization, name):
                    print("Patient removed successfully")
                else:
                    print("Patient not found")
            elif choice == 5:
                break


if __name__ == "__main__":
    app = FrontendManager()
    app.run()
