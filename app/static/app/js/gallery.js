filterSelection("all") // Execute the function and show all columns
function filterSelection(c) {
    var x, i;
    x = document.getElementsByClassName("column");

    // Add the "show" class (display:block) to the filtered elements, and remove the "show" class from the elements that are not selected
    for (i = 0; i < x.length; i++) {
        removeClass(x[i], "show");
        //if (x[i].className.indexOf(c) > -1) addClass(x[i], "show");
        if (isNeedToShow(x[i],c)) addClass(x[i], "show");
    }
}
function isNeedToShow(element, c) {
    if (c == "all") {
        return true;
    }
    var btnContainer = document.getElementById("btnContainer");
    var btns = btnContainer.getElementsByClassName("btn");
    var filterList = [];
    var uniqueFilterList = [];
    for (var i = 0; i < btns.length; i++) {
        if (btns[i].classList.contains("active")) {
            filterList = filterList.concat(btns[i].className.split(" "));
        }
    }
    $.each(filterList, function (i, el) {
        if ($.inArray(el, uniqueFilterList) === -1) uniqueFilterList.push(el);
    });
    uniqueFilterList=uniqueFilterList.filter(function (value, index, arr) {
        return !(["btn", "active", "btnShowAll", "btnColor"].indexOf(value) > -1)
    });
    for (var i = 0; i < uniqueFilterList.length; i++) {
        if (!(element.className.indexOf(uniqueFilterList[i]) > -1)) {
            return false;
        }
    }
    return true;
}



// Show filtered elements
function addClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        if (arr1.indexOf(arr2[i]) == -1) {
            element.className += " " + arr2[i];
        }
    }
}

// Hide elements that are not selected
function removeClass(element, name) {
    var i, arr1, arr2;
    arr1 = element.className.split(" ");
    arr2 = name.split(" ");
    for (i = 0; i < arr2.length; i++) {
        while (arr1.indexOf(arr2[i]) > -1) {
            arr1.splice(arr1.indexOf(arr2[i]), 1);
        }
    }
    element.className = arr1.join(" ");
}

// Add active class to the current button (highlight it)

var btnContainer = document.getElementById("btnContainer");
var btns = btnContainer.getElementsByClassName("btn");
for (var i = 0; i < btns.length; i++) {
    btns[i].addEventListener("click", function () {
        if (this.classList.contains("active")) {
            removeClass(this, "active");
            filterSelection();
            return;
        }
        if (this.classList.contains("btnShowAll")) {
            var btnContainer = document.getElementById("btnContainer");
            var btns = btnContainer.getElementsByClassName("btn");
            for (var i = 0; i < btns.length; i++) {
                removeClass(btns[i]," active")
            }
            this.className += " active";
            filterSelection("all");
            return;
        }
        removeClass(document.getElementsByClassName("btnShowAll")[0]," active");
        var current = this.parentElement;
        current = current.getElementsByClassName("active");
        try {
            if (!this.classList.contains("btnColor")) {
                current[0].className = current[0].className.replace(" active", "");

            } else {
            }
        } finally {
            this.className += " active";
            filterSelection();
        }
    });
}
