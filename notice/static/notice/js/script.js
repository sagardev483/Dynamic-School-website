// Smooth scrolling for navigation links
document.querySelectorAll('.nav-links a').forEach(anchor => {
    anchor.addEventListener('click', (e) => {
        e.preventDefault(); // Prevent default anchor behavior
        const targetId = anchor.getAttribute('href').substring(1); // Extract ID from href
        const targetElement = document.getElementById(targetId);

        // Smooth scroll to the target element
        targetElement?.scrollIntoView({ behavior: 'smooth' });

        // Close the navigation menu after clicking a link (for mobile view)
        if (window.innerWidth <= 768) {
            document.querySelector('.nav-links').classList.remove('active'); // Hide menu on mobile
        }
    });
});

// Get references to modal elements
const modal = document.getElementById("notice-modal");
const noticeBtn = document.getElementById("notice-btn");
const closeBtn = document.querySelector(".close");
const noticesContainer = document.getElementById("notices-container");


// notice ko chalaune chai yahi bata matra ho hai

// Sample Notices Data (can be dynamic if needed)

let notices = []; // Initialize an empty array for notices

document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/notices/')
        .then(response => response.json())
        .then(data => {
            notices = data.notices;  // Assign fetched data to your notices array
            const noticesContainer = document.getElementById("notices-container");
            noticesContainer.innerHTML = "";  // Clear old content

            notices.forEach(notice => {
                const noticeCard = document.createElement("div");
                noticeCard.classList.add("notice-card");

                noticeCard.innerHTML = `
                    <h3>${notice.title}</h3>
                    <p>${notice.description}</p>
                    <small><strong>Date:</strong> ${notice.date}</small>
                    <img src="${notice.image}" alt="Notice Image">
                `;

                noticesContainer.appendChild(noticeCard);
            });
        })
        .catch(error => console.error("Error fetching notices:", error));
});






// Function to load notices into the modal
function loadNotices() {
    noticesContainer.innerHTML = ""; // Clear existing content

    notices.forEach(({ title, description, date, image }) => {
        const noticeCard = document.createElement('div');
        noticeCard.classList.add('notice-card');

        // Creating elements for each notice
        const noticeHTML = `
            <h3>${title}</h3>
            <p>${description}</p>
            <small><strong>Date:</strong> ${date}</small>
            <a href="#" class="read-more" data-image="${image}" data-description="${description}">Read More</a>
        `;
        noticeCard.innerHTML = noticeHTML;

        noticesContainer.appendChild(noticeCard);
    });
}

// Event delegation for handling "Read More" click event
noticesContainer.addEventListener('click', (e) => {
    if (e.target && e.target.classList.contains('read-more')) {
        e.preventDefault();

        const noticeCard = e.target.closest('.notice-card');
        const imageSrc = e.target.dataset.image;
        const description = e.target.dataset.description;

        // Add image dynamically if not already added
        if (!noticeCard.querySelector('.notice-image')) {
            const img = document.createElement('img');
            img.classList.add('notice-image');
            img.src = imageSrc;
            img.alt = description;

            // Insert the image after the notice description
            noticeCard.insertBefore(img, noticeCard.querySelector('small').nextSibling);

            // Hide the "Read More" button after the image is displayed
            e.target.style.display = 'none';
        }
    }
});

// Show the modal and load notices
noticeBtn.addEventListener("click", () => {
    loadNotices();
    modal.classList.add("show"); // Add 'show' class for fade-in effect
});

// Close the modal
closeBtn.addEventListener("click", () => {
    modal.classList.remove("show"); // Remove 'show' class for fade-out effect
});

// Close modal if user clicks outside
window.addEventListener("click", (event) => {
    if (event.target === modal) {
        modal.classList.remove("show");
    }
});

// Header scroll effect
const header = document.querySelector('.header');
window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 50);
});

// Hamburger menu toggle (one listener is sufficient)
const hamburger = document.querySelector('.hamburger');
const navLinks = document.querySelector('.nav-links');
hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    navLinks.classList.toggle('active'); // Show/Hide the nav menu
});

console.log("js is working");