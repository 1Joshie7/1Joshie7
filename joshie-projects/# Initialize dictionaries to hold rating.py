# Initialize dictionaries to hold ratings
ratings = {
    "The Hobbit: The Battle of the Five Armies": [0] * 5,
    "Wonder": [0] * 5
}

def get_rating(movie_name):
    while True:
        try:
            rating = int(input(f"Rate '{movie_name}' (1 to 5): "))
            if 1 <= rating <= 5:
                return rating
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    print("Welcome to the movie rating program!")
    
    # Collect ratings from 15 users
    for i in range(1, 16):
        print(f"\nUser {i}:")
        hobbit_rating = get_rating("The Hobbit: The Battle of the Five Armies")
        wonder_rating = get_rating("Wonder")
        
        # Update ratings count
        ratings["The Hobbit: The Battle of the Five Armies"][hobbit_rating - 1] += 1
        ratings["Wonder"][wonder_rating - 1] += 1

    # Display results
    print("\nRating Summary:")
    
    for movie, counts in ratings.items():
        print(f"\nMovie: '{movie}'")
        print("Rating | Frequency")
        print("------------------")
        for rating in range(1, 6):
            print(f"   {rating}   | {counts[rating - 1]}")
    
if __name__ == "__main__":
    main()

