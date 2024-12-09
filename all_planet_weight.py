# Milestone #2: Adding in All Planets
# Mars is not the only planet in our solar system with its own unique gravity. In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet. Below is a list of the constants for each planet compared to Earth's gravity:

# Mercury: 37.6%

# Venus: 88.9%

# Mars: 37.8%

# Jupiter: 236.0%

# Saturn: 108.1%

# Uranus: 81.5%

# Neptune: 114.0%

# Write a Python program that prompts an Earthling to enter their weight on Earth and then to enter the name of a planet in our solar system. The program should print the equivalent weight on that planet rounded to 2 decimal places if necessary.

# You can assume that the user will always type in a planet with the first letter capitalized and you do not need to worry about the case where they type in something other than one of the above planets.

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# optimized code


# prompt: # prompt: add all in constants Mercury: 37.6%
# # Venus: 88.9%
# # Mars: 37.8%
# # Jupiter: 236.0%
# # Saturn: 108.1%
# # Uranus: 81.5%
# # Neptune: 114.0%

gravity_constants = {
        "Mercury": 37.6,
        "Venus": 88.9,
        "Mars": 37.8,
        "Jupiter": 236.0,
        "Saturn": 108.1,
        "Uranus": 81.5,
        "Neptune": 114.0
    }

#calculate weight
def calculate_weight_on_planets(earth_weight, planet):
      planet = planet.strip().title()
      if planet in gravity_constants:
        weight_on_planet = earth_weight * gravity_constants[planet]
        return f"Your weight on {planet} is: {weight_on_planet:.2f}"
      else:
        return "Invalid planet name."

def main():
   while True:
          try:
             earth_weight = float(input("Enter your weight on Earth: "))
             break
                 
          except ValueError:
              print("Weight must be in a Numeric Value")
  
   planet = input("Enter the name of a planet in our solar system: ")
   print(calculate_weight_on_planets(earth_weight, planet))  

main() 
