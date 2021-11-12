# Group 3's Report on Program Tasks

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Background">Background of Path Planning to Aviation Engineering</a>
    </li>
    <li>
      <a href="#Tools">Introduction of the Engineering Tools</a>
      <ul>
        <li>
          <a href="#Python">Python</a>
        </li>
        <li>
          <a href="#GitHub">GitHub</a>
        </li>
      </ul>
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
            <ul>
              <li>
                <a href="#A_star">A* algorithm</a>
              </li>
              <li>
               <a href="#Dijkstra">Dijkstra's algorithm</a>
              </li>
              <li>
                <a href="#D_star_static">D* algorithm</a>
              </li>
            </ul>
          </ol>
        </li>
      </ol>
    </li>
    <li>  
      <a href="#Summary">Summary</a>
    </li>
    <li>
      <a href="#Contributors">Contributors & Reflections</a>
    </li>
    <li>
      <a href="#References">References</a>
    </li>
  </ol>
</details>


<!-- ABOUT THE PROJECT -->


<a id="Background"></a>
## 1. Background of Path Planning to Aviation Engineering
 <dl> 
<p>Path planning has been an useful method consists of motion planning in different aspects, like self-driving vehicles, humanoid robots, aviation engineering, etc.. In aviation engineering, path planning is one of the important steps before the aircraft starts the journey. </p>

<p>To begin with, the algorithms of path planning is used to compute a continuous path that connecting the start point and the goal point, avoiding collision with obstacles. The path planning algorithms generate a geometric path, passing through free space, as known as C free, from initial point to final point. Since path planning is a procedure that is used to figure out what the status of the area around the starting point and the final point, it is needed to calculate what is the best solution under certain restricts, in order to find out the best route that can avoid obstacles, also the shortest route that can use the least time.</p>

<p>Moreover, without path planning, it is even impossible for us to plan a path. Since without path planning, we could not figure out what is the exact topography, and also other situations that can affect the motion going on the path. It will make the whole motion become way more complicate to go on the path and also increase the percentage of accidents happen. Therefore path planning plays an important role in the every aspects that consist of motion, including flight planning.</p>
  
 <p>Flight path is dependent on the model of the aircraft, including the acoustic characteristics, engine power of the aircraft. Flight path can be different due to the wide range of variables of the aircraft. Therefore, it is important to calculate all the major and minor factors of the aircraft that can affect the flight paths, in order to make a shortest flight path that can have the most cost and time reduction for each particular aircraft.</p> 
 
<p>Flight plans are documents filed by a pilot or flight dispatcher with the local Air Navigation Service Provider (e.g. the FAA in the United States) prior to departure which indicate the plane's planned route or flight path. Flight plan format is specified in ICAO Doc 4444. They generally include basic information such as departure and arrival points, estimated time en route, alternate airports in case of bad weather, type of flight (whether instrument flight rules [IFR] or visual flight rules [VFR]), the pilot's information, number of people on board and information about the aircraft itself. </p>
  
<p>Flight path can be thought of as three-dimensional highways for aircraft. In most land areas of the world, aircraft are required to fly airways between the departure and destination airports. The rules governing airway routing cover altitude, airspeed, and requirements for entering and leaving the airway (see SIDs and STARs). </p>
  
<p>SIDs and STARs are procedures and checkpoints used to enter and leave the airway system by aircraft operating on IFR flight plans. There is a defined transition point at which an airway and a SID or STAR intersect.
A SID (Standard Instrument Departure), defines a pathway out of an airport and onto the airway structure. A SID is sometimes called a Departure Procedure (DP). SIDs are unique to the associated airport.
A STAR(Standard Terminal Arrival Route), ('Standard Instrument Arrival' in the UK) defines a pathway into an airport from the airway structure. STARs can be associated with more than one arrival airport, which can occur when two or more airports are in proximity (e.g., San Francisco and San Jose).</p>

<p>The flight paths are corresponding with several aspects:
First, in the airline prospective, every commercial airline flight start begins with a flight plan. A well-designed flight path can bring great benefits to the airline, including flight safety and economy. For flight safety, an operational flight plan is required to ensure an airplane meets all of the operational regulations for a specific flight, to give the flight crew information to help them conduct the flight safely, and to coordinate with air traffic control (ATC).  For economy, a well-designed flight plan includes the route the crew will fly and specifies altitudes and speeds. It also provides calculations for how much fuel the airplane will use and the additional fuel it will need to carry to meet various requirements for safety. By varying the route (i.e., ground track), altitudes, speeds, and amount of departure fuel, an effective flight plan can reduce fuel costs, time-based costs, overflight costs, and lost revenue from payload that can't be carried, that it leading to saving money for the airline.</p>
  
<p>Next, in the ATC prospective, path planning is crucial in maintaining efficient use of airspace with balance public interest as aircraft operations produces noise to the surrounding community. Therefore, when constructing flight path (SID/STAR) in AIP noise mitigations measures are considered following ICAO guidelines. Take Hong Kong as example, aircraft operations between 11pm to 7am departing east are required to deviate south to the southern district to avoid noise disturbance to the populated areas in both sides of the Victoria harbour.</p>
  
<p>Finally, flight safety is the biggest concern in every controversy in aviation engineering, a well-designed flight path can totally reduce the probability of aviation accident. Some of the unexpected aviation accident due to uncontrollable reasons such as bad weather and extreme topography. A well-designed flight plan can totally avoid the flight path pass through the extreme topography, also, it should including an extra planning to handle emergency situation. For example, the normal flight path should close to the airports for emergency landing or the aircraft can change the flight to the designed emergency path when facing extreme weather.</p>

        
<p>While in this task, we need to design the shortest path in the map which has some obstacles with the basic concepts of flight path planning in the above, including flight safety, flight efficiency and other aircraft operation problem. We need to find a specific aircraft model that costs the minimum in the map, including the time cost, fuel cost and consuming of time, in order to design a cost-efficient flight which is very important in aviation engineering.</p>

  
<a id="Tools"></a>  
## 2. Introduction of the Engineering Tools
  
  <a id="Python"></a>
- ### Python
  <p> Python is the world’s fastest growing programming language, not just amongst software engineers, but also amongst mathematicians, data analysts, etc… since it’s very beginner friendly programming.</p>
  <p> It is created by Guido van Rossum in 1990 as a way to write software for the Amoeba operating system. Python is a general purpose, high level, interpreted language with easy syntax and dynamic semantics programming language. Supports multiple programming paradigms, including procedural, object-oriented, and functional programming. Its high-level built-in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together. Python's simple, easy to learn syntax emphasizes readability and therefore reduces the cost of program maintenance. Python supports modules and packages, which encourages program modularity and code reuse. The Python interpreter and the extensive standard library are available in source or binary form without charge for all major platforms and can be freely distributed. </p> 
  <p>It available on several Operating System including Windows, macOS and Linux.</p> 
    <dd>
      <ul>
        <li> -->Why python is popular:</li>
        <li>1. Easy to learn and use</li> 
        <p>Python language is incredibly easy to use and learn for new beginners and newcomers. The python language is one of the most accessible programming languages available because it has simplified syntax and not complicated, which gives more emphasis on natural language. </p> 
        <li>2.Hundreds of Python Libraries and Frameworks</li> 
        <p>Due to its corporate sponsorship and big supportive community of python, python has excellent libraries that you can use to select and save your time and effort on the initial cycle of development. There are also lots of cloud media services that offer cross-platform support through library-like tools, which can be extremely beneficial.</p>
        <li>3. Big data, Machine Learning and Cloud Computing</li>
        <p>Cloud Computing, Machine Learning, and Big Data are some of the hottest trends in the computer science world right now, which helps lots of organizations to transform and improve their processes and workflows.</p>
        <li>4. Mature and Supportive Python Community</li>
        <p>Python was created more than 30 years ago, which is a lot of time for any community of programming language to grow and mature adequately to support developers ranging from beginner to expert levels. There are plenty of documentation, guides and Video Tutorials for Python language are available that learner and developer of any skill level or ages can use and receive the support required to enhance their knowledge in python programming language.</p>
      </ul>
    </dd>
    
  
  <a id="GitHub"></a>
- ### GitHub
  - GitHub is a code hosting platform for version control and collaboration. It provide a web platform for multiple people to simultaneously write code and come up with new solutions to problems that may arise during the site development process. It lets you and others work together on projects from anywhere. In GitHub, you may 1. create and use a repository 2. start and manage a new branch 3. make changes to a file and push them to GitHub as commits 4.open and merge a pull request. In this group report, we organise and store data in repositories in GitHub. Repositories can contain folders and files, images, videos, spreadsheets, and data sets. We can make and save changes to the files in our repository. GitHub makes it easy to add one at the same time you create a new repository and discuss thing with others.

  
<a id="Task"></a>
## 3. Path Planning Algorithm (Group Task)
  
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
        <p>After making proper modifications to the code, we obtained a satisfactory planning route as the graph shown below.</p>
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/sample.gif" alt="Animated gif demo of the path planning">
        <p>Then, we embedded the data provided by Task 1 into the code and obtained the fuel consumption data of each of the four models in this model. After mathematical comparison and analysis, we agree that PolyU-A380 has the lowest fuel consumption in this model with the cost of 2396.23.</p>
      </dd>
  </dt>
  <dt>
      c) Discussion
      <dd> 
       <p>
         We have used the A* algorithm to compare the costs generated by different aircraft models with the same start and end points, and finally obtain the best results. 
        </p>
        <p>
         Such a research method can be extended and applied to the process of aircraft development: By setting different experimental conditions and using the A* algorithm to calculate the costs for different conditions, the most suitable aircraft parameters can be predicted in a comprehensive manner, providing a good reference for aircraft designers.
       </p>
        <p>
          However, the code is not intelligent enough so far. We tried to let the code compare the data by itself, but failed to do so because the underlying code was too complex. In addition, the path calculated by the A* algorithm maybe not the best since the mechanism of finding the optimal route is based on the closest path between each point itself and the endpoint, rather than considering the whole area. At a later day, we will continue to study in-depth.
        </p>
       </dd>
   </dt>
</dl>
</br>


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
              For 4 constraints with 2 variables, there is no need to consider the path. We can use "Linear programming(LP)" to compute the approximate parameters.
            </li>
            <li>
              For 4 constraints with 6 variables, we have to use A* algorithm to compute the best path due to the changeable T/F_Consuming Area. However, in consideration of the parameters which are integer and the simplification of the constraints, we can easily use the Enumeration Method to find C_T, d_T, C_F, d_F, and then use A* algorithm to enumerate all eligible values of T/F_Consuming Area.
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
  <dt>
      e) Discussion
      <dd>
        <p>
          We used linear programming algorithm as well as A* algorithm to study the aircraft model and successfully found a suitable aircraft model under the constraints. In the process of our research, we successfully developed the LP algorithm and implemented the automatic comparison function of the A* algorithm which means we have established a diversified evaluation system to calculate and predict aircraft design from various aspects. This has helped us tremendously in studying the aircraft model from a different view.
        </p>
        <p>
          Such a diversified research system is of great significance in the development of real aircraft. For example, Linear programming can find the most suitable combination of parameters within the constraints from the perspective of multi-parameter variables; The path planning can analyze the cost-effectiveness of the aircraft model from the perspective of flight cost; Other different approaches can be used to analyze the aircraft model from different aspects. Therefore, a diversified evaluation system can calculate and analyze the model comprehensively, which makes the aircraft design more rigorous, safe and economical.
        </p>
        <p>
          However, we currently have many shortcomings. For instance: LP program is not well developed to handle some special cases correctly; The research method including LP program and A* program can currently only deal with a small number of simple parameters which cannot be synthesized to analyze a large number of aircraft parameters since these programs have narrow application scope, high specificity and poor adaptability. In future studies, we will aim at multifaceted analysis to design methods and programs that can take into account multiple parameters and conditions for evaluation.
        </p>
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
  <dt>
      e) Discussion
      <dd>
        We used the method that traverse the path which had worked out and successfully find the most appropriate minus-cost area.
      </dd>
      <dd>
        To achieve this goal, we have designed some algorithms that can calculate the path in any condition if only the path works out. Furthermore, we also considered two cases, one in which the area is continuous, another one in which the area is discontinous. In this way, we can get more diverse results.
      </dd>
      <dd>
        If this method is improved, it can also be extended to other aspects of area settings, including but not limited to setting optimal climbing and descent areas and calculating the best areas to fly in complex weather conditions. In this sense, it is of great significance for a real flight planning.
      </dd>
      <dd>
        However, in the course of our research, the program we developed is only applicable to the linear search & calculation, which has huge limitations. In the future study, we will focus on more situations, such as planning areas on a map where value is unevenly distributed, or planning two-dimensional areas on a map. We belive that the research in this direction will have greater significance.
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
      <dt>Introduction: </dt>
      <dd>
        This task simulates the planning of a multi-node route in a flight plan.
      </dd>
      <dt>Methodology:</dt>
      <dd>
        After the checkpoints were set, we can achieve it easily by planning between every two points：
      </dd>
      <dt>Result:</dt>
      <dd>
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/Task4_1.gif" alt="continous area">
      </dd>
      <dt>Discussion:</dt>
      <dd>
        Adding checkpoints is a rather easy and straightforward task compared to the others. The most critical part of it is to understand the basic principle that how the algorithm computes the shortest part. Long stories short, we need to know that each shortest path is derived from the other shortest paths. The shortest-circuit path is still the shortest after cutting off the end (National Taiwan Normal University). Therefore, we just need to turn the task of adding checkpoints from a long path into a calculation of the shortest line between each node and connect them together.</dd>
        <dd>
          This task examines our ability to transform the problem. By changing the perspective of the problem, the difficulties can often be solved easier than expected.
  </dt>
  <dt>
    <a id="Task4-2"></a>
    b) <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/eb00ca37d02494c6ea3c81a997bc6d851c3657d0/Source%20codes/Task%204/Changing%20Environment.py">Changing Environment</a>
    <dd>
      <dt>Introduction: </dt>
      <dd>
        This task simulates the performance of the A* algorithm in a complex environment. 
      </dd>
      <dt>Methodology:</dt>
      <dd>
        a) Map generation: Use random numbers and set the probability for each point generation.</br>
        b) Path calculation: use A* algorithm and remove the slash direction
      </dd>
      <dt>Result:</dt>
      <dd>
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/changing%20environment.gif" alt="Changing Environment">
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/T4-2_Bad%20condition_.PNG?raw=true" alt="A* Bad Condition">      
        <p></br>Of course, one day, there will be a chance that the map will then look like the following (www <p>
        <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/ea954d27052beb3984081ce1d04cccbc777cbaf0/Image%20Resources/T4-2_oops....png" width="640px" height="520px" alt="oops...">
      </dd>
      <dt>Discussion:</dt>
      <dd>
        To simplify, this task includes two main points. Firstly, the task requires us to introduce random numbers to create the environment; Secondly, it requires us to restrict some performance of the code to ensure accessibility. The first requirement enables the code to create a random environment, while the second requirement aims to test the algorithm's ability in planning for the shortest path.</dd>
        <dd>
    In the practical aspect, we agree that we have generated a simple idea to form a random environment, which is unneglectable in the flight simulation. The randomly generated environment is also a big challenge for the algorithm. However, although we limit the density of the barriers as well as create some "buff" for the path planner to prove the accessibility of the code, we still can not guarantee that there is always a path between the starting point and the endpoint. We generate the code to let it regenerate a new environment as well as recalculate the ideal path with the shortest distance. When you meet an error in finding the path, a funny message box containing a Chinese notification will be shown on the screen, which is due to the codes shown in the image below.</dd>

![74d98c36aed4f4dd59631ac0649da08](https://user-images.githubusercontent.com/90883440/141282046-33f1ef05-5a31-40af-bf28-a285b11175e0.png)

  
 <dd>
To make the programming more funny, we add a possibility for the code to automatically generate a "wall" to block any possible path. This is in fact related to the code's recauculation capability. However, the A* algorithm prefers to erase memories and regenerate the path due to its design, an update version called D* will be introduced below.
      </dd>
      </br>
  </dt>
  <dt>
    <a id="Task4-3"></a>
    c) <a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/58c8238128de346fe078c0c75ef939a337c4927d/Source%20codes/Task%204/Comparing%20Algorithms.py">Comparing Algoritms</a>
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
          <p>The essential difference between Dijkstra and the breadth-first algorithm (BSF) is that BSF accesses the nodes in the container in an artificially predefined order, while Dijkstra accesses the node with the lowest cumulative cost g(n) (which is the current best estimate of the cumulative cost from the starting node to node "n") in the current container.</p>
<p>The Dijkstra algorithm guarantees that the node it has visited is the least costly node in the container at the current moment, thus ensuring the completeness of the entire algorithm.</p>
          <p>In fact, the A* algorithm we used in the previous task is a variant of Dijkstra's algorithm. This new code takes each new point as a source and produces a shortest path tree by finding the shortest path between this endpoint and all other nodes, which achieves the effect of improving efficiency. However, since its search area is relatively limited compared to Dijkstra's algorithm, the path found is not necessarily the "shortest path".</p>
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
                    In the initial planning, the D* algorithm will start from the end point. Based on a certain point, after searching the points around the store and adding the searched points to the Openlist, the D* algorithm will preferentially traverse the points according to the k-value from smallest to largest and point the pointer to another point whose k-value is smallest. </br>Therefore, D* algorithm is much less efficient than the A* algorithm and does not use its raise and lower part of the algorithm in the initial planning process. Therefore, the D* algorithm does not realize its advantage in static planning.
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
                    <p><a href="https://github.com/Thorkee/ENG1003_w1_Group3/blob/311a7fbff5885b4fff65c018d44d978a1a3e84c5/Source%20codes/Task%204/AlgorithmsLib/d_star_dynamic_QINQijun.py">D* algorithm program</a> 
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
                            Preferentially tranverse the point which is nearest to the end point until it reaches the end. That is similar to dijkstra.
                          </dd>
                          <dt>
                          RAISE state:
                          </dt>
                          <dd>
                          <p>That means current point has changed into obstacle or the value increases. Need to diffuse the obstacles information to surrounding point and to find a point that can reduce the value of current point.</p>
                          <p>There are 3 cases in the next point: 1.New point. 2.This point points to the current point but the value of the next point plus the distance between the two points is not equal to the current point. 3.This point does not point to the current point and the current point can reduce the value of the next point.
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
                    <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/smooth_.png?raw=true" width="320px" height="320px" alt="smooth">
                    <img src="https://github.com/Thorkee/ENG1003_w1_Group3/blob/main/Image%20Resources/not_smooth_.png?raw=true" width="320px" height="320px" alt="not_smooth"> 
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
        <li>
          <dt>
          Discussion
            <dd>
              We have carried out a certain degree of comparison and study of these three algorithms, obtaining the advantages and disadvantages of these three algorithms as well as the scope of application.
            </dd>
            <dd>
              During the development process, we created the same map model and ran the three algorithms in the model while comparing them. In addition, we specifically developed the D* program for representing the dynamic planning function of the D* algorithm. However, during the development process, we encountered a situation where the function could not be implemented referencing the literature. We used the "modeling and large-scale debugging" approach to modify the program based on the feedback from the debug data, and finally implemented the function successfully.
            </dd>
            <dd>
              Furthermore, we have made a greater program design in this study. We improved the algorithm of D* literature to enable the algorithm to implement dynamic planning in more complex environments. Also in the D* program, we added min-heap data structure, which is able to optimize the processing of the minimum k values in the queue. This greatly improves the efficiency of the program in dynamic planning.
            </dd>
            <dd>
              In real life, A* and D* algorithms (and their variants) have wide applications. For example, A* algorithm is often used for common pathfinding problems in applications such as video games and the variant of D* algorithm has used on the Mars rovers Opportunity and Spirit developed by NASA.
            </dd>
            <dd>
              However, the current D* program is not complete and has many bugs, and is not as efficient as we expect it to be. In the future we will focus on fixing bugs and optimizing the program.
            </dd>
          </dt>
        </li>
      </ul>
    </dd> 
  </dt>
</dl>


<a id="Summary"></a>
## 4. Summary
- This freshman program gave us a great challenge. However, we gained a lot of knowledge and experience through this freshman project. From the beginning, we had never touched path planning, never learned python, and didn't even know how to use programming software. In order to complete the task, we had group discussions and kept self-learning. We review a lot of information and do the tast while learning. That led us to learn a lot of algorithms and principles, and gain a lot of experience. In the process, we also developed a passion for programming and algorithms. If there's still a chance, it's sure we'll keep trying to improve ourselves and reach a higher goal!
- We have learned:
  - How to use VScode and Github
  - The Basics of Python
  - How to use Atsushi's A* algorithm to complete the task
  - How to edit the A* algorithm to adapt other tasks
  - Other more algorithms
  - How to program through review literature papers (like D* algorithm)
  - How to use HTML to write the report
  - ...
  - However, the thing that most matters is that we cultivate the ability to learn on our own, to break through from internet resources and to work together as a team to complete tasks with an incredible 1+1>2 effect.


<a id="Contributors"></a>
## 5. Contributors & Reflections

#### LIN Ju @Thorkee
> The process of completing this project was very rewarding. We spent many nights in the library discussing the project until the library closed. Although we did not learn much hard knowledge of path planning or the algorithm in class, we gradually cultivated our independent learning ability in this process, and kept learning from the previous experience and wisdom of the pioneers in this field under the requirements of each task, and created incredible results.
> 
> As the group leader of this group, I did not do a good job in many aspects of leadership. For instance, I did not do a good job in mobilizing members' motivation. I have been reflecting on this and learning from it. I believe I can do better in other tasks in the future. 
> 
> I would also like to take this opportunity to thank my friend QIN Qijun @QuintinUmi. He has a great passion and extraordinary understanding of algorithms and code. He has made a great contribution to the completion of the task. Without him, our task would not have been completed as well as it is now.
> 
> At the same time, I hope that other groupmates could be more motivated to participate in the task. You have done a good job but you could have been more involved in our tasks if you showed your passion earlier. Don't say that it's hard. Every difficulty can be conquered as long as we have passion for it. Equally important, taking a proactive attitude to approach the assigned task is the golden key to reaping great success.
> 
> Lastly, I would like to thank Dr Li-Ta Hsu and Dr Wen as well as Teaching Assistants for giving us such a challenging task. I am very satisfied with the course setup and hope we can continue to work together in the future.

#### Cheng PakHin @marcus2405
> This my first group project to do studying in University, I have learnt a lot through this project. In the task, I and my groupmates are required to collaborate to design the shortest path for a flight plan without crashing on the obstacles. Also, we are needed to calculate the time and cost needed and find out which aircraft model is the most suitable for the flight. We used Python and GitHub to design the flight path. The task required us to read and analyze the code to find out the optimal aircraft model by modifying the data comparing the lowest fuel and time consumption. We used the A* algorithms to compare the costs of the different aircraft models to find out the most suitable aircraft model. Of course, we are not getting the result easily. We have attempted many times. Since this is the first time for me to use Python and typing code, it was quite hard for me typing code on Python at first. But now, I’ve already learnt the basic concept behind the code and how to use them. Besides the technical stuff, I have learnt more about collaboration. During the task, I and my groupmates had many discussions of what parts each of us should do and how to make the group project better in result. 

#### QIN Qijun @QuintinUmi
> This project is the first one I have participated in since I started school.
> 
> This project brought me not only technical improvement, but also teamwork, self-learning ability, perseverance, ability to find solutions to problems... The combination of these qualities. It really makes a person grow and mature.
> 
> In the process of overcoming the project, there is nothing I have experienced more than the word "self-learning". When I was studying algorithms, writing programs and reports, I was often in a state of "learning by doing, learning from doing", not knowing how many difficulties were waiting ahead. But these challenges whetted my appetite for learning algorithm. The intensity and initiative of my study was comparable to my high school days. Finally, live up to expectations, achievements in lage numbers. In this sense, the way Dr. Li-Ta teaches is of great benefit to hardworking students. This way gives us space for independent thinking, self-learning, and teamwork, which can give great growth
> 
> In the future of my life, I will also continue to be looking for my goals, continue to pursue my passions, and devote my passions to the pursuit of my goals!
#### HUI CHIUMING @edmondhui04
> In the past few weeks, we worked together on our group project. Since we are freshman in PolyU, we might both have our own personal activities or school academic works to do, I appreciate all our groupmates are working very hard on this project and take the responsibility to join every group discussion and finish their own distributed works.
> 
>  Charles is very take care of us, he has the team leader characteristic to guide our works, when we are facing difficulties, he always picking times to give assistance or even troubleshooting for us. 
>  
>  Otherwise, in this project, I mainly focus for the collecting research or information for the path planning, writing some codes to form the images then data analysis, finally giving assists and providing some advices for my groupmates. I’ve learnt about the important of path planning, how to use the coding to form some images and using Github to work togethers.
>  
>Finally, This project increase my interest about aviation engineering to learn more and read more.


#### CHENG Wai Ching @Chengmm565
> It was my first project when I got into the university. It was  such a great experience for me to learn from peers and the apply of Python and GitHub. I am responsible for the part of additional tasks which are adding checkpoint and changing environment. In this task, I have to program the route plot from Python and figure out the methodology of adding the nodes. Besides, I have to make changes to the map and finally find the shortest and low-priced path in a complicated environment. Since the coding from Python was quite challenging for me so I asked for assistant from my group mate. Furthermore, I searched and collected information of A* algorithm and Dijkstra’s algorithm from the internet and also some educational video clips from YouTube. 
> 
> From the group work,  we learnt to share different ideas and gained programming skills. We got together and tried to brainstorm a better decision. Our group leader Charles gave us a big support in the group work and he corrected the mistake we made on readme report. It was a precious chance for us to learn from each other.


<a id="References"></a>
## 6. References

1. Atsushi, S., & Nikos, K. (2020). A* grid planning. Retrieved from https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/AStar/a_star.py
2. Atsushi, S. (2020). Grid based Dijkstra planning. Retrieved from https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/Dijkstra/dijkstra.py
3. Atsushi, S. (2020). D* grid planning. Retrieved from https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/DStar/dstar.py
4. An introduction to GitHub. Digital.gov. (2020, June 18). Retrieved November 11, 2021, from https://digital.gov/resources/an-introduction-github/. 
5. Tyagi, N. (2021, February 15). What is Dijkstra's algorithm? examples and applications of Dijkstra's algorithm. What is Dijkstra's Algorithm? Examples and Applications of Dijkstra's Algorithm. Retrieved November 10, 2021, from https://www.analyticssteps.com/blogs/dijkstras-algorithm-shortest-path-algorithm. 
6. 演算法筆記 - Path. National Taiwan Normal University. Retrieved November 11, 2021, from https://web.ntnu.edu.tw/~algo/Path.html
7. Stentz, A. (1994). The D* Algorithm for Real-Time Planning of Optimal Traverses. CARNEGIE-MELLON UNIV PITTSBURGH PA ROBOTICS INST.
8. Carsten, J., Rankin, A., Ferguson, D., & Stentz, A. (2007, March). Global path planning on board the mars exploration rovers. In 2007 IEEE Aerospace Conference (pp. 1-11). IEEE.
 
 
