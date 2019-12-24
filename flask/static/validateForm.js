function printError(elemId, hintMsg) {
    document.getElementById(elemId).innerHTML = hintMsg;
}
function validateForm() {
    var task_name = document.newTaskForm.task_name
    var task_description = document.newTaskForm.task_description
    var task_start_hour = document.newTaskForm.task_start_hour
    var task_start_minutes = document.newTaskForm.task_start_minutes
    var task_end_hour = document.newTaskForm.task_end_hour
    var task_end_minutes = document.newTaskForm.task_end_minutes
    var task_interval = document.newTaskForm.task_interval
    var task_Monday = document.newTaskForm.task_Monday
    var task_Tuesday = document.newTaskForm.task_Tuesday
    var task_Wednesday = document.newTaskForm.task_Wednesday
    var task_Thursday = document.newTaskForm.task_Thursday
    var task_Friday = document.newTaskForm.task_Friday
    var task_Saturday = document.newTaskForm.task_Saturday
    var task_Sunday = document.newTaskForm.task_Sunday

    var nameErr = taskScheduleError =false;

    if (task_name == "") {
        printError("nameErr", "Please enter your name");
        nameErr = true
    }
    if (task_start_hour > task_end_hour) {
        printError("taskScheduleError", "Please make sure your task starts before it ends.")
        taskScheduleError = false
    } else if (task_start_hour == task_end_hour && task_start_minutes > task_end_minutes) {
        printError("taskScheduleError", "Plase make sure your task starts before it ends.")
        taskScheduleError = false
    }
    if (task_start_hour == "") {
        printError("taskScheduleError", "Please add a start hour to your task")
        taskScheduleError = false
    } else if (task_start_minutes == "") {
        printError("taskScheduleError", "Please add a start minute to your task")
        taskScheduleError = false
    } else if (task_end_hour == "") {
        printError("taskScheduleError", "Please add a end hour to your task")
        taskScheduleError = false
    } else if (task_end_hour == "") {
        printError("taskScheduleError", "Please add a end minute to your task")
        taskScheduleError = false
    } else if (task_interval == "") {
        printError("taskScheduleError", "Please add a interval to your task")
        taskScheduleError = false
    }
    if((nameErr || taskScheduleError) == true) {
        return false;}
};