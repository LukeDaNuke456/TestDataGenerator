import random

class Vehicle:
    
    def __init__(self, year, make, model,  mileage, price):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price = price

    def generate_random_mileage(self):
        if self.year == 2024:
            return random.randint(0, 20000)  # New vehicles may have low mileage
        elif self.year == 2023:
            return random.randint(10000, 40000)  # New vehicles may have low mileage
        elif self.year == 2022:
            return random.randint(30000, 80000)  # New vehicles may have low mileage
        elif self.year == 2021:
            return random.randint(50000, 100000)  # One year old vehicles may have higher mileage
        else:
            return random.randint(100000, 200000)  # Older vehicles may have even higher mileage

def autoPopulateVehicles(num_vehicles):
    vehicles = {}

    for i in range(1, num_vehicles + 1):

        vehicles[i] = Vehicle(year=0, make='', model='', mileage=0, price=0)

    return vehicles

def setVehicleYear(vehicles):

    vehicleYear = [2021, 2022, 2023, 2024] 

    for vehicle_id, vehicle in vehicles.items():

        random_make_number = random.randint(0,3)

        if vehicle.year == 0:
            
            vehicle.year = vehicleYear[random_make_number]

def setVehicleMake(vehicles):

    vehicleMake = ['Ford', 'Cheverlet', 'Honda', 'Toyota'] 
    
    for vehicle_id, vehicle in vehicles.items():

        random_make_number = random.randint(0,3)

        if vehicle.make == '':
            
            vehicle.make = vehicleMake[random_make_number]
        
        else: 

            vehicle.model = ''

def setVehicleModels(vehicles):
    
    for vehicle_id, vehicle in vehicles.items():

        # print(str(vehicle.make))

        if vehicle.make == 'Honda':

            vehicle.model = setHondaModels()
            
        elif vehicle.make == 'Toyota':

            vehicle.model = setToyotaModels()
        
        elif vehicle.make == 'Cheverlet':

            vehicle.model = setCheverletModels()
        
        elif vehicle.make == 'Ford':

            vehicle.model = setFordModels()
        
def setToyotaModels():

    toyotaModel = ['Camry', 'Tacoma', 'Tundra', 'Rav4']
    random_make_number = random.randint(0, len(toyotaModel) - 1)
    return toyotaModel[random_make_number]

def setFordModels():

    fordModel = ['F-150', 'F-250', 'Ranger', 'Bronco']
    random_make_number = random.randint(0, len(fordModel) - 1)
    return fordModel[random_make_number]

def setHondaModels():

    hondaModel = ['Accord', 'Civic', 'Passport', 'Ridgeline']
    random_make_number = random.randint(0, len(hondaModel) - 1)
    return hondaModel[random_make_number]

def setCheverletModels():

    cheverletModel = ['Silverado 1500', 'Camaro', 'Impala', 'Malibu']
    random_make_number = random.randint(0, len(cheverletModel) - 1)
    return cheverletModel[random_make_number]
    
def setVehicleMiles(vehicles):

    for vehicle_id, vehicle in vehicles.items():

        if vehicle.mileage == 0:
            vehicle.mileage = vehicle.generate_random_mileage()

def main():

    while True: 

        print("How many vehicle's do you want in your inventory? : ")
        num_of_vehicles = input()
            
        if num_of_vehicles.isdigit():

            num_of_vehicles = int(num_of_vehicles)

            vehicles = autoPopulateVehicles(num_of_vehicles)
            setVehicleYear(vehicles)
            setVehicleMake(vehicles)
            setVehicleModels(vehicles)
            setVehicleMiles(vehicles)
            print("---------------------------------\n")

            for vehicle_id, vehicle in vehicles.items():
                print(f"Vehicle ID: {vehicle_id}")
                print(f"Year: {vehicle.year}")
                print(f"Make: {vehicle.make}")
                print(f"Model: {vehicle.model}")
                print(f"Mileage: {vehicle.mileage} miles\n")
            
            print("---------------------------------\n")

            break

        else: 

          print("Not a number. How many vehicle's do you want in your inventory? : ")  


if __name__ == "__main__":
    main()
# def populate_arrays():

   




