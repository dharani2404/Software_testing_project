script.js

let students = [];

window.onload = function () {
    const data = localStorage.getItem("students");
    if (data) {
        students = JSON.parse(data);
    }
    populateStudentTable();
    populateGradeTable();
    showSection("studentList");
};

document.getElementById("enrollmentForm").addEventListener("submit", function(event) {
    event.preventDefault(); 

    var student = {
        name: document.getElementById("name").value,
        fatherName: document.getElementById("fatherName").value,
        dob: document.getElementById("dob").value,
        gender: document.getElementById("gender").value,
        bloodGroup: document.getElementById("bloodGroup").value,
        address: document.getElementById("address").value,
        email: document.getElementById("email").value,
        contact: document.getElementById("contact").value,
        grade: "Pending"
    };

    students.push(student);
    alert(student.name + " was enrolled successfully");
    localStorage.setItem("students", JSON.stringify(students));
    populateStudentTable();
    populateGradeTable();
    document.getElementById("enrollment").style.display = "none"; 
    resetForm();
});

function toggleEnrollment() {
    let enrollmentSection = document.getElementById("enrollment");
    enrollmentSection.style.display = enrollmentSection.style.display === "none" ? "block" : "none";
}

function resetForm() {
    document.getElementById("enrollmentForm").reset();
}

function showSection(sectionId) {
    document.querySelectorAll("section").forEach(section => section.style.display = "none");
    document.getElementById(sectionId).style.display = "block";
}

function populateStudentTable() {
    let tbody = document.querySelector("#studentsTable tbody");
    tbody.innerHTML = "";

    students.forEach(student => {
        let row = document.createElement("tr");
        row.innerHTML = `<td>${student.name}</td><td>${student.fatherName}</td><td>${student.gender}</td>
        <td>${calculateAge(student.dob)}</td><td>${student.bloodGroup}</td><td>${student.address}</td>
        <td>${student.contact}</td><td>${student.email}</td>`;
        tbody.appendChild(row);
    });
}

function calculateAge(dob) {
    let birthDate = new Date(dob);
    let ageDiff = Date.now() - birthDate.getTime();
    let ageDate = new Date(ageDiff);
    return Math.abs(ageDate.getUTCFullYear() - 1970);
}

function populateGradeTable() {
    let tbody = document.querySelector("#gradesTable tbody");
    tbody.innerHTML = "";

    students.forEach((student, index) => {
        let row = document.createElement("tr");
        row.innerHTML = `<td>${student.name}</td>
        <td><input type="text" value="${student.grade}" onchange="updateGrade(this, ${index})"></td>
        <td><button onclick="saveGrade(${index})">Save</button></td>`;
        tbody.appendChild(row);
    });
}

function updateGrade(input, index) {
    students[index].grade = input.value;
}

function saveGrade(index) {
    alert(`Grade for ${students[index].name} saved successfully!`);
    localStorage.setItem("students", JSON.stringify(students));
}

function searchStudents() {
    let query = document.getElementById("searchBox").value.toLowerCase();
    let tbody = document.querySelector("#studentsTable tbody");
    tbody.innerHTML = "";

    let filtered = query
        ? students.filter(student => student.name.toLowerCase().includes(query))
        : students;

    filtered.forEach(student => {
        let row = document.createElement("tr");
        row.innerHTML = `<td>${student.name}</td><td>${student.fatherName}</td><td>${student.gender}</td>
        <td>${calculateAge(student.dob)}</td><td>${student.bloodGroup}</td><td>${student.address}</td>
        <td>${student.contact}</td><td>${student.email}</td>`;
        tbody.appendChild(row);
    });
}