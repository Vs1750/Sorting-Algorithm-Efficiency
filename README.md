# Sorting Algorithm Efficiency
#### Video Demo:  <https://www.youtube.com/watch?v=h-Z8V5eik4k>
### Description:
I created a web page with Flask, Python, HTML, CSS and JavaScript.
The web page investigates the efficiency of five different sorting algorithms: bubble sort, selection sort, insertion sort, merge sort and quick sort.

### How to use it:
- The user can either choose one of nine buttons, which generate a list of N unordered numbers, or input the numbers manually.

- Then, the user clicks 'run' to run the sorting algorithms. 

- The output and the time taken to execute the program are then displayed in each grey box. The name of the algorithm and the times will turn green once the numbers have finished sorting.

- If the user wants to stop the program or reset the web page, they can click 'Stop/Reset'.

- The user should only enter numbers in the text box, and separate the numbers with commas or spaces. An error message will be displayed below the text box, specifying the type of error.

- Two times are displayed: the CPU time taken to execute the program, and the elapsed time starting from when the user clicks a button until the output is displayed.

A small note about the times is given at the bottom of the web page.

At the footer, there is a GitHub logo on the right which redirects to my GitHub profile when clicked. I also used an online template for the footer, and used the same design for the header.\
Source of the footer template: <https://www.quackit.com/html/html_editors/scratchpad/?example=/html/templates/footers/minimalist_single_line_footer>

I used Bootstrap v5.3 so that the web page looks better. The classes that I frequently used are `.row .col .col-# .mb-# .mt-# .fs-# .btn`. I also used Jinja's `for` loop to avoid repeating the five output rows, which keeps the HTML cleaner.

### JavaScript functions:
#### Some JavaScript functions, especially those that handle JSON, were written with help from Claude.
Here are the helper functions I used in the web page:
```
1. parseNumbers(text)
```
- This function parses the input from the user to remove extra spaces and commas so the function returns an array of numbers, such as `[5, 7, 2, 8, 2.5, -3]`.

```
2. shuffledSequence(number)
```
- This function is for the nine buttons with random N numbers. It takes in a list of ordered N numbers, and shuffles them with the Fisher-Yates shuffle algorithm. Then, the shuffled list is passed to the sorting algorithm.

```
3. requestData(algorithm, numbers, signal)
```
- This function takes the input and sends it to the benchmark route from app.py.

```
4. showResults(data, start_time)
```
- This function calculates the total time elapsed using `start_time`, as well as displaying the output and the two times using `getElementById()`.
- This function also changes the color of the texts the name of the algorithm and the two times by adding the class `.completed` to the elements with those ids.

```
5. showError(message)
```
- Displays the error message in the error box.

```
6. clearInput()
```
- Clears the input box.

```
7. clearData(algorithm)
```
- Clears the output text box and the times.
- I did not combine this with `clearInput()` because `clearInput()` is called once in the Reset handler, so I kept the two separate.
- If I combine `clearInput()` and `clearData(algorithm)` together, I would have clear the input text box five times, which is redundant.

```
8. removeColor(algorithm)
```
- Removes the green color from the name and times (essentially removing the class ".completed").
- I did not combine `clearData()` and `removeColor(algorithm)` because there is no need to clear the output box and times, because the loading animation replaces them when a run starts.
- So, `clearData(algorithm)` is only called when the Stop/Reset button is clicked, and `removeColor(algorithm)` is called every time any button is clicked.

```
9. loading(algorithm)
```
- Displays a loading animation.
- Processing → Processing. → Processing.. → Processing...

```
10. setDisabled(flag)
```
- Disables the buttons and the input text box while the program is being executed.

### app.py
#### There are three functions: 
```
1. index()
```
- Renders index.html

```
2. algo(algorithm, numbers)
```
- Takes the sorting algorithm and the list of numbers as arguments.
- It calculates the time taken by the CPU by executing the sorting process three times, and gets the median of the times.
- Then, it returns the output (sorted numbers) and the median of the times

```
3. benchmark()
```
- Reads the JSON data from the request.
- This function takes `data`, a dictionary with two key-value pairs.
- The first key-value pair is `"algorithm"` and the name of the algorithm, such as `"bubble"` or `"merge"`.
- The second is `"numbers"`, whose value is a list of numbers.

- An error message is returned when:
    - the data is not a dictionary,
    - the data is missing the algorithm or numbers key, or either is empty,
    - the algorithm name is not one of the five supported algorithms,
    - the numbers are not a list,
    - the list contains more than 100,000 numbers,
    - a number is not an `int` or a `float`,
    - a boolean expression is in the numbers list (since `True` is technically the integer 1).

- If everything works fine, this function returns a dictionary `{"name": algorithm, "sorted": sorted_list, "time": median_time}`, which Flask converts to JSON. 

#### app.py also imports a dictionary with key-value pairs, each with the name of the algorithm and the actual function.
```
from algorithms import ALGORITHMS
```
In the algorithms file, there are five files of different sorting algorithms.

I ran into a problem: quick sort worked with the `1 - 1,000` button but failed when I typed the numbers 1 to 1000 in order. The terminal showed `RecursionError: maximum recursion depth exceeded`. I believe this happens because the last element, which is the largest in a sorted list, is used as the pivot. To prevent this, I swap a randomly chosen element with the last element before partitioning.
