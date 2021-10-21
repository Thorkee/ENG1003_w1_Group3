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
          <a href="#Task1">Find the PolyU Aircraft Model that achieve minimum cost for the challenge assigned to your group (Task1)</a>
        </li>
        <li>
          <a href="#Task2">Calculate the Minimum Cost Aircraft Model within the Constrains (Task2)</a>
        </li>
        <li>
          <a href="#Task3">Design a minus-cost for the route (Task3)</a>
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
     <a href="#References">References</a>
    </li>
</details>


<!-- ABOUT THE PROJECT -->


<a id="Background"></a>
## 1. Background of Path Planning to Aviation Engineering


<a id="Task"></a>
## 2. Path Planning Algorithm (Group Task)


<a id="Task1"></a>
### i.Find the PolyU Aircraft Model that achieve minimum cost for the challenge assigned to your group (Task1)
  <dl>
  <dt>
    a) Introduction 
    <dd>
     <p>The first task required us to read and analyze the code to find the optimal aircraft model by modifying the data to compare the lowest fuel consumption of the four pre-defined aircraft under the optimal path.
     </dd>
  </dt>
  <dt>
      b) Designing Scheme
      <dd>  
<p>For the first step, we changed the specific data(See <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Source%20codes/Task%201.py">here</a>) from the code downloaded from the class GitHub repository. By studying and analyzing the code, we found that the establishment of boundaries and barriers is based on mathematical function logic. 

<p>After making proper modifications to the code, we obtained a satisfactory planning route as the graph shown below.

![Animated gif demo of the path planning](https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/sample.gif)

<p>Then, we embedded the data provided by Task 1 into the code and obtained the fuel consumption data of each of the four models in this model. After mathematical comparison and analysis, we agree that PolyU-A380 has the lowest fuel consumption in this model with the cost of 2396.23.
</dd>
  </dt>
  <dt>
      c) Reflection on Task 1
  <dd> 
 <p> After Task 1, we reflected on the content of the task and concluded the following issues that could be improved:
 <p> 1. The code is not intelligent enough. We tried to let the code compare the data by itself, but failed to do so because the underlying code was too complex.
  <p>2. Since the mechanism of finding the optimal route is based on the closest path between each point itself and the end point, rather than considering the whole area and the consumption per unit of different area to get the lowest consumption route, this code logic is not promising enough to find the most ideal route of different models with least fuel consumption. 
 <p> 3. In the context of the situation mentioned in the second point, the logic of finding the best route is very rigid, causing inefficiencies in the code in complex environments.
 <p> 4. In order to improve the problems mentioned in the second and third points, we tried the code of other logics. The results are presented in the last part.

<a id="Task2"></a>
### ii.Calculate the Minimum Cost Aircraft Model within the Constrains (Task2) 
<dl>
  <dt>
    a) Introduction 
    <dd>
      In this part, our group aimed to find the model that costs least in specific map. To do this, we designed two programs for different targets including time-cost, fuel-     cost, time-comsuming area cost and fuel-comsuming area cost. In addition, one(<a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/1d72155688cf89cc3575e87390523b05672b62a5/Source%20codes/Task%202_46_DCTnFA.py">A* Path Algorithm</a>) of the programs, which is improved by our group from A*_search_algorithm whose author is Atsushi Sakai Nikos Kanargias, is to calculate the minimum cost route, and the other one(<a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/f1e17513fd60dc90df051e24e3ff09c5147ba4ca/Source%20codes/Task%202_42.py">LP Algorithm</a>) which is entirely programmed by us is to calculate the parameters of the model within the constrains.(<a href="#T2_result">See the result directly</a>)
    </dd>
  </dt>
  <dt>
      b) Designing Scheme
      <dd>
        <p>Through the research, we found that the parameters of the model do not affect the minimum-cost except the time and fuel consuming area. </p>       
        (It can prove by: Cost = (C_T * d_T + C_F * d_F) * Distance(a) + C_T/F_Area * Distance(b). If only C_T * d_T + C_F * d_F = Constant !=0, the shortest Distance will not change) 
        <p>With this idea, 
          <ul>
            <li>
              For 4 constraints with 2 variables, there is no need to consider the path. We can use the "Linear programming(LP)" to compute the approximate paramaters.
            </li>
            <li>
              For 4 constraints with 6 variables, we have to use A* algorithm to compute the best path due to the changeable T/F_Consuming Area. However, in consideration of the paramaters which are integer and the simplification of the constrains, we can easily use Enumeration Method to find C_T, d_T, C_F, d_F, and then use A* algorithm to enumerate all eligible value of T/F_Consuming Area.
            </li>
          </ul>
      </dd>
  </dt>
  <dt>
      c) Algorithm Implementation
      <ul>
        <li>
          <p><a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/f1e17513fd60dc90df051e24e3ff09c5147ba4ca/Source%20codes/Task%202_42.py">LP Algorithm</a></p>
          <ul>
            <li>List of key function:</li>
            <ul>
              <li>Search for Cross Point</li>
              <li>Calculate Target Line</li>
              <li>Display</li>  
            </ul>
            <li>
              <p>-->Search for Cross Point</p>
              Substitute every x in domain into every Line Equation. If |f(x) - g(x)| --> 0, then mark the point(x, f(x)) and store it into list A. Adjusting the precision to ensure the efficiency and accuracy is the key point. The accuracy will decrease if the slops of the two lines are too similar.
            </li>
            <li>
              <p>-->Calculate Target Line</p>
              First, determine whether the point in A is in the spacific area between certain line and xy-aixs and store the results of every line into list B. Take the intersection of the B, and then we can get the possible points.</br>
              Second, find the minimum point using the equation C_F = (C_T * d_T) / d_F(i.e. f(x) = (a * x) / b. However, there may be some BUGs like no appropriate point or the result which goes to infinity. We just consider general condition and there is considerable scope for improvement.
            </li>
            <li>
              <p>-->Display</p>
              Show the result with pattern and figure.
            </li>
          </ul>
        </li>
        <li>
          <p><a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/1d72155688cf89cc3575e87390523b05672b62a5/Source%20codes/Task%202_46_DCTnFA.py">A* Path Algorithm</a></p>
          <ul>
            <li>List of key function:</li>
            <ul>
              <li>Basic Path-Computing Function</li>
              <li>Enumeration and Comparation Function</li>
              <li>Display Result</li>  
            </ul>
            <li>
              <p>-->Basic Path-Computing Function</p>
              Theory: Start at a curtain point, retrieve every direction to find the next minimum point (The direction closest to the goal will be the first to be retrieve), move to next point and repeat above step.</br>
              Actually, this algorithm is based on Breadth-First Search, but will firstly search the point that has the shortest distance to the goal. That can improve the efficiency in some cases.
            </li>
            <li>
              <p>-->Enumeration and Comparation Function</p>
              Enumerate all possible value within the constrains and find the minimum value for the paramaters.
            </li>
            <li>
              <p>-->Display Result</p>
              In this part, we will show all the infomation including computing process, approximate paramaters, the minimum cost, the new and origin route.
            </li>
          </ul>
        </li>
      </ul>
  </dt>
  <dt>
  <a id="T2_result"></a>
      d) Result
      <dd>
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
        <br>
        <p>--------------------------------------------------------:P---------------------------------------------------------------</p>
        </br>
        <p>Figure 2: The Progress & Result of 4 Constraints with 6 Variables</p>
        On the left side, there is the progress of computing and the result of the paramaters.</br>
        On the right side, there is the path of new model(red) and the origin model(gray)
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/af85185020bca6497db33ecd4020a62654ab06d0/Image%20Resources/T2-46....png" alt="4 Constraints with 6 Variables Result">
      </dd>
  </dt>
</dl>
    

<a id="Task3"></a>
### iii.Design a minus-cost for the route(Task3)
<img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/905ea6c99b122458a3358c8c6a43f88a1d47bbe1/Image%20Resources/not%20continous%20area.png" alt="not continous area">
<img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/905ea6c99b122458a3358c8c6a43f88a1d47bbe1/Image%20Resources/continous%20area.png" alt="continous area">


<a id="Task4"></a>
### iv.Task title (Task4)


<a id="Contributors"></a>
## 3. Contributors

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

## 4. References







