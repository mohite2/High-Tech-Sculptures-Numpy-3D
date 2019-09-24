## IS590PR assignment 4: "High-Tech Sculptures" 
### (Manipulating Numpy 3D arrays)


Complete this solution program so that all Doctests work properly and it solves 
the problems described.  Some empty functions are included to help guide you. 
You may add or modify their parameters and may create additional functions as 
well.

### The Scenario:
Suppose we are trying to carve a lasting sculpture from a "marble" block, and its
intended final 3D shape is given with a 3D array, containing just 1s and 0s to 
indicate where it will be solid vs empty (removed).

We also have a large rectangular prism of floats in a 3D array. These numbers
represent local densities within a block of marble, perhaps having been measured 
externally using some scanning process like NMR (nuclear magnetic resonance) 
from 3 axes.

Before we 'carve' or 'sculpt' the shapes from these expensive marble blocks, 
we want to determine which is the best orientation (rotation) to use for each 
one. 'Best' will be determined by calculating mean density and stability of the 
sculptures that would result.

The output should look similar to this, but these numbers are made up. 
Within each block's results, order by stability, then by density (descending):

    Shape File: shape_1.npy
        Block File: marble_block_X.npy   
        Rotation: 180 axis 0 to 1                  Mean density: 78.24  Stable
        Rotation: 180 axis 0 to 1, 90 axis 1 to 2  Mean density: 48.24  Stable
        Rotation:  90 axis 1 to 2                  Mean density: 64.11  Unstable
        ...
        
        Block File: marble_block_Y.npy
        ...

    Shape File: shape_2.npy
        Block File: marble_block_X.npy   
        Rotation: 180 axis 0 to 1                  Mean density: 82.04  Stable
        Rotation:  90 axis 1 to 2                  Mean density: 64.11  Unstable
        Rotation: 180 axis 0 to 1, 90 axis 1 to 2  Mean density: 48.24  Unstable
        ...
        


1.	Which block & orientation results in the highest average density, AFTER 
    being 'carved'. I gave you five block data files, but write your program 
    so that it can read and evaluate MANY such files -- break your habits of 
    copy-and-paste programming now!  :-)   Your output should display the 
    answer along with the block's filename and the rotations used. TIPS: You'll 
    need the Numpy nanmean() function to get the correct density. For that, 
    you'll find it overflows with the float16 dtype we have. So convert use 
    astype('float32') before calling nanmean().
2.	For each possible orientation, determine if the sculpture would be 
    stable & balanced without tipping or leaning. So, you need to compute where 
    the center of mass would be and make sure it's within the horizontal 
    boundaries of its base.
    
Use the SciPy package function to compute the center of mass.
See https://docs.scipy.org/doc/scipy-1.3.0/reference/generated/scipy.ndimage.center_of_mass.html

These Khan Academy pages on Center of Mass are helpful to understand problem 2:

•	https://www.khanacademy.org/science/physics/linear-momentum/center-of-mass/v/center-of-mass-equation

•	https://www.khanacademy.org/science/physics/linear-momentum/center-of-mass/a/what-is-center-of-mass
    (the "Topple Limit" section in this page helps explain problem 2 above. 
    But you are not required to compute tipping angles)
    
### Steps to Get Started (mostly shown in class):

0. Do this assignment individually (no teams, so you won't have any problems with git merge conflicts.)
1. Create one and only one fork of this repository.  
2. In the GitHub website, immediately go to your new repository,
3. click "Settings" tab
4. click "Collaborators & Teams"
5. click the X to REMOVE the "All_Students" team from having access to your repository.  **Warning!**  We'll deduct 20% from your score if you don't.
6. Return to the \<Code\> tab in YOUR new repository in GitHub.
7. Click "Clone or Download" to get the link you need for PyCharm.
8. As shown in the video and in class session 4, create a new PyCharm project from your repository.
9. Now in PyCharm, write the code needed to make the existing functions and all tests work properly.
10. COMMIT AND PUSH revisions **frequently** as you work on it, until complete.
11. INCLUDE the output text file in your GitHub repository to make checking your calculations easier.


REQUIRED: 
To get full credit, complete the functions and program to solve the questions above. 
Also _one_ of these things:

A.  Write enough Doctests in your program so that the Doctests With Coverage 
report in PyCharm shows at least 80% actual coverage for the 
numpy_marble_solution.py file. **OR**

B.  Configure TravisCI to work on your repository and showing proof, such 
taking a screenshot of your build history and committing that screen shot image 
into your GitHub repository where we can see it.  Remember you get TravisCI 
free as part of the GitHub "StudentPack". I have even included a working .travis.yml 
configuration file to make this much easier. 
 