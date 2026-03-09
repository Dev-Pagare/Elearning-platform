document.addEventListener('DOMContentLoaded', function () {
    const container = document.getElementById('course-container');
    if (!container) return;

    fetch('/all_courses/')
        .then(r => r.json())
        .then(data => {
            const courses = data.courses;

            if (!courses || courses.length === 0) {
                container.innerHTML = `
                    <div style="grid-column:1/-1;text-align:center;padding:3rem;color:#6b7280;">
                        <i class="bi bi-journal-x" style="font-size:2.5rem;margin-bottom:1rem;display:block;"></i>
                        <p style="font-size:1rem;font-weight:600;">No courses available yet.</p>
                    </div>`;
                return;
            }

            container.innerHTML = '';

            courses.forEach(course => {
                const priceHTML = (!course.price || course.price == 0)
                    ? `<span class="course-price-free">Free</span>`
                    : `<span class="course-price">&#8377;${parseFloat(course.price).toFixed(0)}</span>`;

                const categoryLabel = course.category
                    ? course.category.charAt(0).toUpperCase() + course.category.slice(1)
                    : 'Course';

                // Short description — 100 characters max
                const shortDesc = course.description
                    ? (course.description.length > 100
                        ? course.description.substring(0, 100) + '...'
                        : course.description)
                    : 'Learn practical skills with expert guidance in this comprehensive course.';

                const card = document.createElement('div');
                card.className = 'gallery';
                card.innerHTML = `
                    <div class="course-img-wrap">
                        <img src="${course.image_url}" alt="${course.course_name}" loading="lazy">
                        <div class="course-category-tag">${categoryLabel}</div>
                    </div>
                    <div class="course-card-body">
                        <div class="desc">${course.course_name}</div>
                        <p class="course-short-desc">${shortDesc}</p>
                        <div class="course-price-row">
                            ${priceHTML}
                            <div class="course-rating">
                                <i class="bi bi-star-fill"></i>
                                <span>4.8</span>
                            </div>
                        </div>
                        <a href="/course_description_page/?course_id=${course.course_id}"
                           class="button-29">View Course &rarr;</a>
                    </div>`;

                container.appendChild(card);
            });
        })
        .catch(err => {
            console.error('Error:', err);
            container.innerHTML = `
                <div style="grid-column:1/-1;text-align:center;padding:3rem;color:#ef4444;">
                    <p>Failed to load courses. Please refresh the page.</p>
                </div>`;
        });
});