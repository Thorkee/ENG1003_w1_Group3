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
              <a href="#Task4-3">Comparing Algoritms</a>
            <ol>
              <li>
                <a href="#A_star">A* algorithm</a>
              </li>
              <li>
               <a href="#Dijkstra">Dijkstra's algorithm</a>
              </li>
            <li>
              <a href="#D_star_static">D* algorithm</a>
            </li>
          </ol>
        </li>
      </ol>
    </li>
    <li>  
      <a href="#Summary">Summary</a>
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
 <dl> 
      <p>Path planning has been an useful method consists of motion planning in different aspects, like self-driving vehicles, humanoid robots, aviation engineering, etc.. In aviation engineering, path planning is one of the important steps before the aircraft starts the journey. In this task, we need to design the shortest path in the map which has some obstacles. Also, cost calculation is an important step when we are designing the path. We need to find a specific aircraft model that costs the minimum in the map, including the time cost, fuel cost and consuming of time, in order to design a cost-efficient flight which is very important in aviation engineering.

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
   <ol>
     <li> The code is not intelligent enough. We tried to let the code compare the data by itself, but failed to do so because the underlying code was too complex.</li>
     <li> Since the mechanism of finding the optimal route is based on the closest path between each point itself and the end point, rather than considering the whole area and the consumption per unit of different area to get the lowest consumption route, this code logic is not promising enough to find the most ideal route of different models with least fuel consumption. </li>
     <li> In the context of the situation mentioned in the second point, the logic of finding the best route is very rigid, causing inefficiencies in the code in complex environments.</li>
     <li> In order to improve the problems mentioned in the second and third points, we tried the code of other logics. The results are presented in the last part.</li>
    </ol>
   </dd>
   </dt>

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
        (It can prove by: Cost = (C_T * d_T + C_F * d_F) * Distance(a) + C_T/F_Area * Distance(b). If only C_T * d_T + C_F * d_F = Constant ≠ 0, the shortest Distance will not change) 
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
              <p>--> Search for Cross Point</p>
              Substitute every x in domain into every Line Equation. If |f(x) - g(x)| --> 0, then mark the point(x, f(x)) and store it into list A. Adjusting the precision to ensure the efficiency and accuracy is the key point. The accuracy will decrease if the slops of the two lines are too similar.
            </li>
            <li>
              <p>--> Calculate Target Line</p>
              First, determine whether the point in A is in the spacific area between certain line and xy-aixs and store the results of every line into list B. Take the intersection of the B, and then we can get the possible points.</br>
              Second, find the minimum point using the equation C_F = (C_T * d_T) / d_F(i.e. f(x) = (a * x) / b. However, there may be some BUGs like no appropriate point or the result which goes to infinity. We just consider general condition and there is considerable scope for improvement.
            </li>
            <li>
              <p>--> Display</p>
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
</br></br>

<a id="Task3"></a>
### iii.Design a minus-cost area for the route (Task3)
<dl>
  <dt>
    a) Introduction 
    <dd>
      In this task, our group has designed two algorithms to find the minus-cost area in order to decrease the cost of flight. Based on the limitation that the maximun minus-cost area is 16 grids, there are two programs, one (<a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/e23231d680f2e3812cf2e1b7f342bf5a4af754cd/Source%20codes/Task%203_not_continuous_area.py">Discontinuous Area Algorithm</a>) of which is to calculate discontinous area, and another one (<a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/e23231d680f2e3812cf2e1b7f342bf5a4af754cd/Source%20codes/Task%203_continuous_area.py">Continuous Area Algorithm</a>) is to calculate continous area. (<a href="#T3_result">See the result directly</a>)
    </dd>
  </dt>
  <dt>
      b) Designing Scheme
      <dd>
        <p>Through analysing, we believed that covering the minus-area on the route which has worked out is the efficient way to reduce the cost of flight. </p>       
        <p>According to this principal, we can</p>
          <ol>
            <li>
              Compute the route of flight without covering the minus-area.
            </li>
            <li>
              Traverse the route which has worked out and record the data.
            </li>
            <li>
              Process and compare the data, get the result. 
            </li>
          </ol>
      </dd>
  </dt>
  <dt>
      c) Algorithm Implementation
      <ul>
        <li>
          <p><a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/e23231d680f2e3812cf2e1b7f342bf5a4af754cd/Source%20codes/Task%203_not_continuous_area.py">Discontinuous Area Algorithm</a></p>
          <ul>
            <li>List of key function:</li>
            <ul>
              <li>A* Path Algorithm</li>
              <li>Discontinous Area Algorithm</li>
              <li>Display</li>  
            </ul>
            <li>
              <p>--> A* Path Algorithm</p>
              Search for the minimum-cost path.
            </li>
            <li>
              <p>--> Discontinous Area Algorithm</p>
              1) Traverse the path, while recording firstly all slash paths and secondly all straight paths.</br>
              2) Append all the slash path into minus-cost area list. If there is still avialable space of the list, append the straight path into the list.</br>
            </li>
            <li>
              <p>--> Display</p>
              Draw all the blue areas recorded in the minus-cost list on the map.
            </li>
          </ul>
        </li>
        <li>
          <p><a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/e23231d680f2e3812cf2e1b7f342bf5a4af754cd/Source%20codes/Task%203_continuous_area.py">Continuous Area Algorithm</a></p>
          <ul>
            <li>List of key function:</li>
            <ul>
              <li>A* Path Algorithm</li>
              <li>Continous Area Algorithm</li>
              <li>Display</li>  
            </ul>
            <li>
              <p>--> A* Path Algorithm</p>
              Search for the minimum-cost path.
            </li>
            <li>
              <p>--> Continous Area Algorithm</p>
              Traverse the path. Different from the Discontinous Area Algorithm, this traversal is like a "snake". The "snake" will firstly come out from the start point. Then with the head of the "snake" moving on, its body will come out and follow one by one (Maximum length is 16 grid). If the "snake" meets the fuel/time cost areas, it will disappear and come out from other sides of the areas.</br></br>
              During the process of traversal, we have to record the position where the "snake" can reduce the cost most.</br>
            </li>
            <li>
              <p>--> Display</p>
              Draw the blue "snake" at the position on the map.
            </li>
          </ul>
        </li>
      </ul>
  </dt>
  <dt>
  <a id="T3_result"></a>
      d) Result
      <dd>
        Through computing, we got following minus-cost area:      
        <ul>
          <li>
            Discontinous Area shown below:
            <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/905ea6c99b122458a3358c8c6a43f88a1d47bbe1/Image%20Resources/not%20continous%20area.png" alt="not continous area">
          </li>
          </br></br>
          <li>
            Continous Area shown below:
            <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/905ea6c99b122458a3358c8c6a43f88a1d47bbe1/Image%20Resources/continous%20area.png" alt="continous area">
          </li>
        </ul>
      </dd>
  </dt>
</dl>
</br></br>

<a id="Task4"></a>
### iv.Additional Tasks (Task4)
<dl>
  <dt>
    <a id="Task4-1"></a>
    a) <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/eb00ca37d02494c6ea3c81a997bc6d851c3657d0/Source%20codes/Task%204/Adding%20Checkpoints.py">Adding Checkpoints</a>
    <dd>
      <p>
        This task simulates the planning of a multi-node route in a flight plan.</br>
        We can achieve it by planning between every two points：</br>
      </p>
      <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/Task4_1.gif" alt="continous area">
    </dd>
  </dt>
  <dt>
    <a id="Task4-2"></a>
    b) <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/eb00ca37d02494c6ea3c81a997bc6d851c3657d0/Source%20codes/Task%204/Changing%20Environment.py">Changing Environment</a>
    <dd>
      </br>
      This task simulates the performance of the A* algorithm in a complex environment. </br>
      a) Map generation: Use random numbers and set the probability for each point generation.</br>
      b) Path calculation: use A* algorithm and remove the slash direction</br>
      <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/changing%20environment.gif" alt="Changing Environment">
      <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/T4-2_Bad%20condition_.PNG?raw=true" alt="A* Bad Condition">      
      <p></br>Of course, one day, there will be a chance that the map will then look like the following (w <p>
      <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/ea954d27052beb3984081ce1d04cccbc777cbaf0/Image%20Resources/T4-2_oops....png" width="640px" height="520px" alt="oops...">
    </dd>
  </dt>
  <dt>
    <a id="Task4-3"></a>
    c)Comparing Algoritms
    <dd>
      <ul>
        <li>
          <a id="A_star">
          a. <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/311a7fbff5885b4fff65c018d44d978a1a3e84c5/Source%20codes/Task%204/AlgorithmsLib/a_star.py">A* algorithm</a>
            <p>
              A* algorithm absorbs the advantages of Dijkstra algorithm. Similar to Dijkstra algorithm, A* algorithm also adopts priority queue. What different from Dijkstra is that A* algorithm sets priority follow the equation "f(n) = g(n) + h(n)", which can optimize the tranversal efficiently and reduce the time consumption in some cases. 
            </p>
            <p>Advantage:</p>
            <ul>
              <li>
                A* algorithm can substantially optimize the process of searching and reduce the time of calculating, which can improve the capability of path planning in all areas like flight planning. 
              </li>
            </ul>
            </p>
            <p>Disadvantage:</p>
            <ul>
              <li>
                A* algorithm is mainly suitable for static calculation. If there are some changes like obstacles suddenly appearing in the path which has worked out, this algorithm have to recalculate the path. That will cause the time comsumption and effect the performance of computing. If there is no optimization for A* algorithm, this algorithm will be difficult to apply for dynamic planning.
              </li>
            </ul>
            </p>
        </li>
        <li>      
          <a id="Dijkstra"></a>
          b. <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/311a7fbff5885b4fff65c018d44d978a1a3e84c5/Source%20codes/Task%204/AlgorithmsLib/dijkstra.py">Dijkstra's algorithm</a>
          <p>Dijkstra&#39;s algorithm is an algorithm designed by computer scientist Edsger W. Dijkstra in 1956 that uses a similar approach to breadth-first search to solve the shortest path problem for a single source in a given environment (especially if the environment is already given).</p>
          <p>In fact, the A\* code we used in the previous task is a variant of Dijkstra&#39;s algorithm. This new code takes each new point as a source and produces a shortest path tree by finding the shortest path of this vertex and all other nodes.</p>
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/DJ%20vs%20A%20STAR.gif" alt="demo of dij alg">  
        </li>
        <li>
          <a id="D_star_static"></a>
          c. <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/311a7fbff5885b4fff65c018d44d978a1a3e84c5/Source%20codes/Task%204/AlgorithmsLib/d_star_dynamic_QINQijun.py">D* algorithm</a> 
          <p>
          D* algorithm is based on Dijkstra algorithm. The difference is that the D* algorithm will first start searching from the end point. After initial planning, if an obstacle is detected, the program will make local adjustment to avoid the obstacle. Until it reaches the end, the program ends.
          </p>
            <ol>
              <li>
                <ul>         
                  <li>
                    <p>Static planning</p>
                    In the initial planning, the D* algorithm will start from the end point. Based on a certain point, after searching the points around the store and adding the searched points to the Openlist, the D* algorithm will preferentially traverse the points according to the k-value from smallest to largest and point the pointer to another point whose k-value is smallest. Therefore, D* algorithm is much less efficient than the A* algorithm and does not use its raise and lower part of the algorithm in the initial planning process. Therefore, the D* algorithm does not realize its advantage in static planning.
                  <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/FOOLISH%20D%20STAR.gif" alt="FD">
                  </li>
                  <li>
                    <p>Dynamic planning</p>
                    <p>
                    After the initial planning, when an obstacle is detected and blocks the route, the D* algorithm will first diffuse the RAISE state (indicating that the actual value of the current point is higher than the originally calculated point) from the obstacle point to the surrounding points, until it diffuses to the point or path that can reduce the actual value, and diffuses the LOWER state (indicating that the actual value of the current point can be reduced by other points) to the diffusion source, until it gets the new shortest path, then ending the obstacle avoidance planning. In this way, the D* algorithm can efficiently re-route when the route is blocked, enabling dynamic planning.
                    </p>
                    <p>
                    Of course, to reflect the efficient dynamic planning of D* algorithm, the program must be run on a larger scale map to ensure that the area that its RAISE state spreads takes a very small percentage of the map, otherwise the efficiency of D* algorithm replanning will not be comparable to that of A* algorithm replanning.
                    </p>
                    <p>
                    In order to implement dynamic planning to demonstrate the function of D* algorithm, group member QIN Qijun studied a lot of D* theory literature papers, and modified part of the algorithm theory in the literature papers through a lot of experimental data and reasoning. Finally, he independently finished a program based on D* algorithm and almost implemented the function of dynamic planning. The dynamic planning function shows below:
                    <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/DYNAMIC.gif" alt="DD">
                    </p>
                  </li>
                </ul>
              </li>
              <li>
                Algorithm Implementation
                <ul>
                  <li>
                    <p><a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/e23231d680f2e3812cf2e1b7f342bf5a4af754cd/Source%20codes/Task%203_not_continuous_area.py">Discontinuous Area Algorithm</a></p>
                    <ul>
                      <li>Structure of program:</li>
                      <ul>
                        <li>MAP</li>
                        <li>OPENLIST</li>
                        <li>DSTAR.state_process</li>
                        <li>DSTAR.obstacle_sensor</li>  
                        <li>DSTAR.run</li>
                      </ul>
                      <li>
                        <p>--> MAP</p>
                        To record the information of every point on the map.
                      </li>
                      <li>
                        <p>--> OPENLIST</p>
                        We use the minimum binomial heap to implement the OPENLIST function and assign key values (not k values in D*) to all elements in OPENLIST to maintain the uniqueness of the elements and to update the element values.
                      </li>
                      <li>
                        <p>--> DSTAR.state_process</p>
                        To process current point and build the relationship with other point.
                        <dl>
                          <dt>
                          NORMAL state:
                          </dt>
                          <dd>
                            Preferentially tranverse the point which is nearest to the end point similar to dijkstra until it reaches the end.
                          </dd>
                          <dt>
                          RAISE state:
                          </dt>
                          <dd>
                          <p>That means current point has changed into obstacle or the value increases. Need to diffuse the obstacles information to surrounding point and to find a point that can reduce the value of current point.</p>
                          <p>There are 3 cases in the next point: 1.New point. 2.The next point points to the current point but the value of the next point plus the distance between the two points is not equal to the current point. 3.The next point does not point to the current point and the current point can reduce the value of the next point.
                          </dd>
                          <dt>
                          LOWER state:
                          </dt>
                          <dd>
                            That means the value of current point can be reduce by surrounding point which is closer to the starting point and diffuse value-decreasing information to the new obstacles. In addition, change the direction of that point.
                          </dd>
                        </dl>
                      </li>
                      <li>
                        <p>--> DSTAR.obstacle_sensor</p>
                          This is a function for detecting obstacles. In practical applications, we can pass in signals from actual sensor devices. If the sbstacles block the original route, the program will execute obstacles avoidance function.
                      </li>
                      <li>
                        <p>--> DSTAR.run</p>
                        Integrates pathfinding and obstacle avoidance functions. It is the main function of DSTAR.
                      </li>
                    </ul>
                  </li>
                </ul>
              </li>
              </br>
              <li>
                Development History
                <dl>
                  <dd>
                  </br>
                    <p>
                      Limited by our technical level, The total development time of the D* algorithm program was about a month. At the beginning we used Mr. Atsushi's D* algorithm template and referred to a lot of literature papers. Everything went well in the initial planning process. However, when an obstacle suddenly appeared, the program could only be replanned if the obstacle was smooth, otherwise the program would hang. 
                    </p>
                    <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/smooth_.png?raw=true" width="360px" height="360px" alt="smooth">
                    <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/not_smooth_.png?raw=true" width="360px" height="360px" alt="not_smooth"> 
                    <p></br> 
                      So we created a small map and then did a lot of debugging. We obtained a lot of experimental data including but not limited to the processing of each point to the next point in different situations, the change of data near the diffusion source at the beginning of diffusion and the change of the pointer during the diffusion process. Eventually we boldly modified and adjusted part of the algorithm in the diffusion process, and successfully implemented obstacles avoidance action.
                    </p>
                    <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/edit.PNG?raw=true" alt="algorithm_adjust">
                    <p></br> 
                      However, such forced changes may create potential BUGs. So there are lot of experimentation and modification needed to ensure the program's viability.
                    </p>
                  </dd>
                </dl>
              </li>
              <li>
                Problem still unresolved
                <dl>
                  <dd>
                  </br>
                    <p>
                    Currently there is a situation that causes replanning to hang, that is, when the two replanned diffusion ranges overlap, the last diffusion may form a ring in the previous diffusion range, causing the program to spin around in the ring. 
                    </p>
                    <p>
                    We speculate that it may be due to the fact that the h-values of some points were modified and not equal to the k-values during the next diffusion, causing these points to interfere with the program's judgment during the next diffusion. 
                    </p>
                    <p>
                    If conditions permit, we will try our best to fix BUGs and improve the program.
                    </p>
                  </dd>
                </dl>
              </li>
            </ol>          
        </li>   
      </ul>
    </dd>   
</dl>


<a id="Summary"></a>
## 3. Summary
- This freshman program gave us a great challenge. However, we gained a lot of knowledge and experience through this freshman project. From the beginning, we had never touched path planning, never learned python, and didn't even know how to use programming software. In order to complete the task, we had group discussions and kept self-learning. We review a lot of information and do the tast while learning. That led us to learn a lot of algorithms and principles, and gain a lot of experience. In the process, we also developed a passion for programming and algorithms. If there's still a chance, it's sure we'll keep trying to improve ourselves and reach a higher goal!
- We have learned:
  - How to use VScode and Github
  - The Basics of Python
  - How to use Atsushi's A* algorithm to complete the task
  - How to edit the A* algorithm to adapt other task
  - Other more algorithms
  - How to programmed through review literature papers (like D* algorithm)
  - How to use HTML to write the report
  - ...


<a id="Contributors"></a>
## 4. Contributors

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

<a id="References"></a>
## 5. References


