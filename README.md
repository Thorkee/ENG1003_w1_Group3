# Group 3's Report on Compulsory Tasks

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Background">Background of Path Planning to Aviation Engineering</a>
    </li>
    <li>
      <a href="#Task">Path Planning Algorithm (Group Task)</a>
      <ol>
        <li>
          <a href="#Task1">Task title (Task1)</a>
        </li>
        <li>
          <a href="#Task2">Task title (Task2)</a>
        </li>
        <li>
          <a href="#Task3">Task title (Task3)</a>
        </li>
        <li>
          <a href="#Task4">Task title (Task4)</a>
        </li>
      </ol>
    </li>
    <li>
      <a href="#Contributors">Contributors</a>
    </li>
    <li>
     <a href="#4.References">References</a>


<!-- ABOUT THE PROJECT -->


<a id="Background"></a>
## Background of Path Planning to Aviation Engineering


<a id="Task"></a>
## Path Planning Algorithm (Group Task)


<a id="Task1"></a>
#### i.Find the PolyU Aircraft Model that achieve minimum cost for the challenge assigned to your group (Task1)
For the first step, we changed the specific data from the code downloaded from the class GitHub repository. By studying and analyzing the code, we found that the establishment of boundaries and barriers is based on mathematical function logic. 

It is worth mentioning that we also changed the slash density inside the code in order to solve the problem that the planning points would cross the slash. Eventually, after making suitable modifications to the code, we obtained a satisfactory planning route as the graph shown below.

![Animated gif demo of the path planning](https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/sample.gif)

Then, we embedded the data provided by Task 1 into the code and obtained the fuel consumption data of each of the four models in this model. After mathematical comparison and analysis, we agree that PolyU-A380 has the lowest fuel consumption in this model.

After Task 1, we reflected on the content of the task and concluded the following issues that could be improved:
  1. The code was not intelligent enough. We tried to let the code compare the data by itself, but failed to do so because the underlying code was too complex.
  2. Since the mechanism of finding the optimal route is based on the closest path between each point itself and the end point, rather than considering the whole area and the consumption per unit of different area to get the lowest consumption route, this code logic is not promising enough to find the most ideal route of different models with least fuel consumption. 
  3. In the context of the situation mentioned in the second point, the logic of finding the best route is very rigid, causing inefficiencies in the code in complex environments.
  4. In order to improve the problems mentioned in the second and third points, we tried the code of other logics. The results are presented in the last part.

<a id="Task2"></a>
#### ii.Task title (Task2)

<a id="Task3"></a>
#### iii.Task title (Task3)

<a id="Task4"></a>
#### iv.Task title (Task4)


<a id="Contributors"></a>
## Contributors

#### LIN Ju @Thorkee
> Responsible part:

#### Cheng PakHin @marcus2405
> Responsible part:

#### QIN Qijun @QuintinUmi
> Responsible part:

#### HUI CHIUMING @edmondhui04
> Responsible part:

#### CHENG Wai Ching @Chengmm565
> Responsible part:

## References







