# SwimTrainingGenerator
A program to create personalized swimming training plans for swimmers of all levels.

# Description

SwimTrainingGenerator is a program designed to help swimmers create customized training plans based on their available equipment and desired training intensity. The program splits the training into three key components: warm-up, main set, and cool-down.

- Users input their preferences through a pop-up window, including available materials and training intensity (easy, normal, or hard).
- The program generates a random training plan tailored to the input, ensuring that harder trainings are longer and more challenging.
- The training plan is printed to the console, with a clear breakdown of each segment.

Here is your training plan:

Warm-up:
2 x 300m IM

Main set:
4 x 400m Breast, w/ Kickboard
2 x 150m IM, drills
2 x 50m Breast, kick
1 x 400m Back, kick, w/ Kickboard
2 x 25m Back, drills, w/ Kickboard
2 x 200m IM, kick, w/ Kickboard
1 x 150m Fly, kick

Cool down:
600m choice

Total Training Distance: 4200m

# Installation

This program does not require additional installations. However, users need:
- A Python interpreter (version 3.7 or higher).
- An IDE or terminal for running the program.
To install Python, visit [python.org](https://www.python.org/downloads/).



# Usage

To use the SwimTrainingGenerator:
1. Navigate to the `__main__.py` file in the project directory.
2. Run the program:
3. A pop-up window will appear to collect user preferences. The training plan will be displayed in the console. 

 
# Limitations

During the development of this project i was faced by some difficulties to include both randomness in the training while also having the training make sense. This means to not have super long single exercises followed by a really short one followed by long one again. In swimming a lot of times on a higher level during each training the focus is put on a specific topic. This couldn't be accounted for in this program and is clearly a limitation.
Furthermore, a limiting factor to the effectivness of the swim training generator, is that there is no time included. Meaning that the swimmer/user choses their own time to swim 100meters or 50meters etc. For beginners to intermediates, this is not a problem however for expert swimmers, the measurement of improvement is mostly time, meaning that in a training usually they are given certain times to complete a specific length. This was difficult to account for, since we are not sure how fast the swimmers usually swim and what would be an appropriate time for each swimmer and each stroke. This would require some collaboration with a professional swim coach. 

# Contributions
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch:
    git checkout -b your_branch or click "new branch" on github
3. Submit a pull request.


Contributions addressing the limitations of including time that adapts to the level of the swimmer and introducing a theme for each swim training to focus on to make it more coherent, are especially welcome. 


# License 
The project is licensed under the MIT License. See the [License] file for details.

# Aids
For this project i used ChatGPT for code refinement in some cases, mostly helping to structure the GUI file. No other aids were used.


## Authors
[Johannes Hendrix] (https://github.com/johanneshendrix/SwimTrainingGenerator)- Initial work








