# RACE PACE

## By Mark Todman

![Launch page screenshot.](/assets/images/readme-images/race-pace-amiresponsive.png)

The deployed [Race Pace](https://race-pace-marktodman.herokuapp.com/) app.

The [GitHub repository.](https://github.com/marktodman/race-pace)

---
## OVERVIEW

1. [Race Pace Concept](#Race-Pace-Concept)
2. [How to use Race Pace](#How-to-use-Race-Pace)
3. [Planning](#Planning)
4. [Testing](#Testing)
5. [Deployment](#Deployment)
6. [Future Development Ideas](#Future-development-ideas)
7. [Credits](#Credits)

## RACE PACE CONCEPT

Race Pace is an online application for calculating finish times in popular running race distances: Marathon, Half Marathon, 10km and 5km. Race Pace allows the user to calculate either the pace required to reach a target race finish time, or their race finish time if they run at a user-specified average pace. 

Race Pace will also provide split information to help guide the runner through their race. The split information is times that the runner should be passing certain distance markers in their race. 

Race Pace will work in either kilometers or miles based on the user's preference.

### Target Audience:

- Runners who want to know how to pace their race to achieve a target finish time.
- Runners who want to know what their finish time will be if they run a particular pace in their race.
- Runners who want to improve their race times and race pacing.
- Coaches working with runners to improve their race times and race pacing.

## HOW TO USE RACE PACE

Users are guided through screens to generate the pacing information. Race Pace returns personalised information, so the first stage is for the user to input their first name.

The user selects their race distance: Marathon, Half Marathon, 10km, 5km. All calculations will be based on their selection.

The user selects their prefered units: kilometers or miles. All calculations will be based on their selection.

The user can then select whether they have a target finish time and would like to calculate the required pace to achieve the target. Or, whether they have a target pace and would like to know what finish time this would produce in their race.

Once this selection is made Race Pace calculates and returns the finish time and the pace, together with split times for given distance markers in the race.

## Features

The app is designed to guide the user through the necessary steps to calculate their race pace to acheive their race goals. As the app is hosted in a terminal display, this has been centred on the page. A background image of runners provides context to the app. The RACE PACE title text (named 'speed' on [figlet.org](http://www.figlet.org/fontdb_example.cgi?font=speed.flf)) is coloured in white and green to ephamise that the app is designed for race pacing.

![Screenshot of Race Pace start page.](assets/images/readme-images/race-pace-screenshot.png)

To personalise the UX, the first stage is for the user to input their first name. Only alpha characters are accepted and numbers or blanks will return an error.

![Example of numeric input error.](assets/images/readme-images/numeric-name-error.png)

The app provides feedback on each input so the user can see their input. This is especially useful in free input. Text that the user has input is printed with blue text on a white background, The user has the chance to 'Restart' if they decide they have made an error at any stage.

![Name input feedback.](assets/images/readme-images/name-input.png)

The app is menu driven to reduce user typograph error and enhance UX. Each menu contains users options which direct the user through a pathway to deliver a race pace, race time and race splits. The menu options provide user choice and control, allowing defensive coding to protect the app and produce the desired output for the user. 'Exit' and 'Restart' options exist on each menu. 'Exit' closes the app. Once closed the user can restart by clicking the 'Start Race Button' which is always present onscreen. 'Restart' starts the app from the beginning, allowing the user to enter a new name and continuing through the menus from the start.




