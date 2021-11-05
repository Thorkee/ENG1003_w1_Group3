# Group 3's Report on Compulsory Tasks

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
          <a href="#Task1">Find the PolyU Aircraft Model that achieve minimum cost for the challenge assigned to your group (Task1)</a>
        </li>
        <li>
          <a href="#Task2">Calculate the Minimum Cost Aircraft Model within the Constrains (Task2)</a>
        </li>
        <li>
          <a href="#Task3">Design a minus-cost area for the route (Task3)</a>
        </li>
        <li>
          <a href="#Task4">Additional Tasks (Task4)</a>
          <ol>
            <li>
              <a href="#Task4-1">Adding Checkpoints</a>
            </li>
            <li>
              <a href="#Task4-2">Changing Environment</a>
            </li>
            <li>
              <a href="#Comparing Algoritms">Comparing Algoritms</a>
            <ol>
            <li>
               <a href="#Dijkstra's algorithm">Dijkstra's algorithm</a>
              </li>
            <li>
              <a href="#D* algorithm">D* algorithm</a>
            </li>
          </ol>
        </li>
      </ol>
    </li>
    <li>
      <a href="#Contributors">Contributors</a>
    </li>
    <li>
     <a href="#References">References</a>
    </li>
</details>
    
<a id="Background"></a>
**1. Background of Path Planning to Aviation Engineering**

Path planning has been an useful method consists of motion planning in different aspects, like self-driving vehicles, humanoid robots, aviation engineering, etc. In aviation engineering, path planning is one of the important steps before the aircraft starts the journey. In this task, we need to design the shortest path in the map which has some obstacles.

Also, cost calculation is an important step when we are designing the path. We need to find a specific aircraft model that costs the minimum in the map, including the time cost, fuel cost and consuming of time, in order to design a cost-efficient flight which is very important in aviation engineering.

<a id="Task"></a>
**2. Path Planning Algorithm (Group Task)**

<a id="Task1"></a>
i.　_Find the PolyU Aircraft Model that achieve minimum cost for the challenge assigned to your group (Task1)_

**a) Introduction**

The first task required us to read and analyze the code to find the optimal aircraft model by modifying the data to compare the lowest fuel consumption of the four pre-defined aircraft under the optimal path.

**b) Designing Scheme**

For the first step, we changed the specific data(See [here](https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Source%20codes/Task%201.py)) from the code downloaded from the class GitHub repository. By studying and analyzing the code, we found that the establishment of boundaries and barriers is based on mathematical function logic.

After making proper modifications to the code, we obtained a satisfactory planning route as the graph shown below.

![Animated gif demo of the path planning](https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/sample.gif)

Then, we embedded the data provided by Task 1 into the code and obtained the fuel consumption data of each of the four models in this model. After mathematical comparison and analysis, we agree that PolyU-A380 has the lowest fuel consumption in this model with the cost of 2396.23.

**c) Reflection on Task 1**

After Task 1, we reflected on the content of the task and concluded the following issues that could be improved:

The code is not intelligent enough. We tried to let the code compare the data by itself but failed to do so because the underlying code was too complex.

Since the mechanism of finding the optimal route is based on the closest path between each point itself and the end point, rather than considering the whole area and the consumption per unit of different area to get the lowest consumption route, this code logic is not promising enough to find the most ideal route of different models with least fuel consumption.

In the context of the situation mentioned in the second point, the logic of finding the best route is very rigid, causing inefficiencies in the code in complex environments.

In order to improve the problems mentioned in the second and third points, we tried the code of other logics. The results are presented in the last part.

<a id="Task2"></a>
ii.　_Calculate the Minimum Cost Aircraft Model within the Constrains (Task2)_

**a) Introduction**

In this part, our group aimed to find the model that costs least in specific map. To do this, we designed two programs for different targets including time-cost, fuel-     cost, time-comsuming area cost and fuel-comsuming area cost. In addition, one(<a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/1d72155688cf89cc3575e87390523b05672b62a5/Source%20codes/Task%202_46_DCTnFA.py">A* Path Algorithm</a>) of the programs, which is improved by our group from A*_search_algorithm whose author is Atsushi Sakai Nikos Kanargias, is to calculate the minimum cost route, and the other one(<a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/f1e17513fd60dc90df051e24e3ff09c5147ba4ca/Source%20codes/Task%202_42.py">LP Algorithm</a>) which is entirely programmed by us is to calculate the parameters of the model within the constrains.(<a href="#T2_result">See the result directly</a>)

**b) Designing Scheme**

Through the research, we found that the parameters of the model do not affect the minimum-cost except the time and fuel consuming area.

(It can prove by: Cost = (C\_T \* d\_T + C\_F \* d\_F) \* Distance(a) + C\_T/F\_Area \* Distance(b). If only C\_T \* d\_T + C\_F \* d\_F = Constant !=0, the shortest Distance will not change)

With this idea,

For 4 constraints with 2 variables, there is no need to consider the path. We can use the &quot;Linear programming(LP)&quot; to compute the approximate parameters.

For 4 constraints with 6 variables, we have to use A\* algorithm to compute the best path due to the changeable T/Consuming Area. However, in consideration of the parameters which are integer and the simplification of the constrains, we can easily use Enumeration Method to find C\_T, d\_T, C\_F, d\_F, and then use A\* algorithm to enumerate all eligible value of T/Consuming Area.

**c) Algorithm Implementation**

[_ **LP Algorithm** _](https://github.com/Thorkee/ENG1003_w1_Group3/blob/f1e17513fd60dc90df051e24e3ff09c5147ba4ca/Source%20codes/Task%202_42.py)

List of key function:

1. Search for Cross Point
2. Calculate Target Line
3. Display

**Search for Cross Point**

Substitute every x in domain into every Line Equation. If |f(x) - g(x)| --\&gt; 0, then mark the point(x, f(x)) and store it into list A. Adjusting the precision to ensure the efficiency and accuracy is the key point. The accuracy will decrease if the slops of the two lines are too similar.

**Calculate Target Line**

First, determine whether the point in A is in the spacific area between certain line and xy-aixs and store the results of every line into list B. Take the intersection of the B, and then we can get the possible points.

Second, find the minimum point using the equation C\_F = (C\_T \* d\_T) / d\_F(i.e. f(x) = (a \* x) / b. However, there may be some BUGs like no appropriate point or the result which goes to infinity. We just consider general condition and there is considerable scope for improvement.

**Display**

Show the result with pattern and figure.

[_ **A\* Path Algorithm** _](https://github.com/Thorkee/ENG1003_w1_Group3/blob/1d72155688cf89cc3575e87390523b05672b62a5/Source%20codes/Task%202_46_DCTnFA.py)

List of key function:

1. Basic Path-Computing Function
2. Enumeration and Comparation Function
3. Display Result

**Basic Path-Computing Function**

Theory: Start at a curtain point, retrieve every direction to find the next minimum point (The direction closest to the goal will be the first to be retrieve), move to next point and repeat above step.
 Actually, this algorithm is based on Breadth-First Search, but will firstly search the point that has the shortest distance to the goal. That can improve the efficiency in some cases.

**Enumeration and Comparation Function**

Enumerate all possible value within the constrains and find the minimum value for the

parameters.

**Display Result**

In this part, we will show all the information including computing process, approximate parameters, the minimum cost, the new and origin route.

<a id="T2_result"></a>
**d) Result**

Through computing, we got following model and data:
        <table width="100%" border="0" cellspacing="1" cellpadding="4" bgcolor="#cccccc" class="tabtop13" align="center">
            <tr>
              <th colspan="8">4 Constraints with 2 Variables</th>
            </tr>
            <tr>
              <td>&nbsp;</td>
              <td width="8%" class="btbg font-center">𝐶_𝐹</td>
              <td width="8%" class="btbg font-center">d_𝐹</td>
              <td width="8%" class="btbg font-center">𝐶_T</td>
              <td width="8%" class="btbg font-center">d_T</td>
              <td width="8%" class="btbg font-center">C_C</td>
              <td width="8%" class="btbg font-center">d_F_A</td>
              <td width="8%" class="btbg font-center">d_T_A</td>
            </tr>
            <tr>
              <th width="8%" class="btbg font-center" rowspan="2">Group 1 Aircraft Model</th>
              <td width="8%" class="btbg font-center">20</td>
              <td width="8%" class="btbg font-center">5</td>
              <td width="8%" class="btbg font-center">20</td>
              <td width="8%" class="btbg font-center">5</td>
              <td width="8%" class="btbg font-center">10</td>
              <td width="8%" class="btbg font-center">5</td>
              <td width="8%" class="btbg font-center">5</td>
            </tr>     
            <tr>
              <th width="8%" class="btbg font-center" colspan="7">Total Cost: 24448.52559935244</th>
            </tr>
            <tr>
              <th width="8%" class="btbg font-center" colspan="8">4 Constraints with 6 Variables</th>
            </tr>
            <tr>
              <td width="8%" class="btbg font-center"></td>
              <td width="8%" class="btbg font-center">𝐶_𝐹</td>
              <td width="8%" class="btbg font-center">d_𝐹</td>
              <td width="8%" class="btbg font-center">𝐶_T</td>
              <td width="8%" class="btbg font-center">d_T</td>
              <td width="8%" class="btbg font-center">C_C</td>
              <td width="8%" class="btbg font-center">d_F_A</td>
              <td width="8%" class="btbg font-center">d_T_A</td>
            </tr>
            <tr>
              <th width="8%" class="btbg font-center" rowspan="2">Group 1 Aircraft Model</th>
              <td width="8%" class="btbg font-center">9</td>
              <td width="8%" class="btbg font-center">2</td>
              <td width="8%" class="btbg font-center">1</td>
              <td width="8%" class="btbg font-center">8</td>
              <td width="8%" class="btbg font-center">10</td>
              <td width="8%" class="btbg font-center">9</td>
              <td width="8%" class="btbg font-center">1</td>
            </tr>         
            <tr>
              <th width="8%" class="btbg font-center" colspan="7">Total Cost: 4274.2349903979</th>
            </tr>
        </table>
        <p>Figure 1: The Result of 4 Constraints with 2 Variables</p>
        This is the result computed by LP Algorithm shown as figure.
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/task2_1.png" alt="4 Constraints with 2 Variables Result">
 

Figure 1: The Result of 4 Constraints with 2 Variables

Figure 2: The Progress &amp; Result of 4 Constraints with 6 Variables

On the left side, there is the progress of computing and the result of the parameters.

On the right side, there is the path of new model(red) and the origin model(gray)

<a id="Task3"></a>
_iii. Design a minus-cost area for the route (Task3)_

<a id="Task4"></a>
_iv.Additional Tasks (Task4)_

<a id="Task4-1"></a>
1. **Adding Checkpoints**
      <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/Task4_1.gif" alt="continous area">

<a id="Task4-2"></a>
1. **Changing Environment**
      
<a id="Comparing Algoritms"></a>
1. **Comparing Algorithms**
  1. A\*

 <a id="Dijkstra's algorithm"></a>
  1. Dijkstra Algorithm

Dijkstra&#39;s algorithm is an algorithm designed by computer scientist Edsger W. Dijkstra in 1956 that uses a similar approach to breadth-first search to solve the shortest path problem for a single source in a given environment (especially when the environment is defined).

In fact, the A\* code we used in the previous task is a variant of Dijkstra&#39;s algorithm. This new code takes each new point as a source and produces a shortest path tree by finding the shortest path of this vertex and all other nodes.
          
   <a id="D* algorithm"></a>
  1. D\*
