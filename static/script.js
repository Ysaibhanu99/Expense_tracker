// ======================================
// EXPENSE TRACKER — CLIENT-SIDE SCRIPT
// ======================================

document.addEventListener("DOMContentLoaded", function () {

    // -----------------------------------------
    // 1. Auto-set today's date in the date input
    // -----------------------------------------
    const dateInput = document.getElementById("date");
    if (dateInput && !dateInput.value) {
        const today = new Date();
        const yyyy = today.getFullYear();
        const mm = String(today.getMonth() + 1).padStart(2, "0");
        const dd = String(today.getDate()).padStart(2, "0");
        dateInput.value = `${yyyy}-${mm}-${dd}`;
    }


    // -----------------------------------------
    // 2. Delete confirmation
    // -----------------------------------------
    const deleteForms = document.querySelectorAll(".delete-form");
    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (e) {
            const confirmed = confirm("Are you sure you want to delete this expense?");
            if (!confirmed) {
                e.preventDefault();
            }
        });
    });


    // -----------------------------------------
    // 3. Basic form validation — prevent amount <= 0
    // -----------------------------------------
    const expenseForm = document.getElementById("expense-form");
    if (expenseForm) {
        expenseForm.addEventListener("submit", function (e) {
            const amountInput = document.getElementById("amount");
            const amount = parseFloat(amountInput.value);

            if (isNaN(amount) || amount <= 0) {
                e.preventDefault();
                amountInput.focus();
                amountInput.style.borderColor = "#ef4444";
                amountInput.style.boxShadow = "0 0 0 3px rgba(239, 68, 68, 0.15)";

                setTimeout(function () {
                    amountInput.style.borderColor = "";
                    amountInput.style.boxShadow = "";
                }, 2000);
            }
        });
    }


    // -----------------------------------------
    // 4. Edit form validation
    // -----------------------------------------
    const editForm = document.getElementById("edit-form");
    if (editForm) {
        editForm.addEventListener("submit", function (e) {
            const amountInput = document.getElementById("amount");
            const amount = parseFloat(amountInput.value);

            if (isNaN(amount) || amount <= 0) {
                e.preventDefault();
                amountInput.focus();
                amountInput.style.borderColor = "#ef4444";
                amountInput.style.boxShadow = "0 0 0 3px rgba(239, 68, 68, 0.15)";

                setTimeout(function () {
                    amountInput.style.borderColor = "";
                    amountInput.style.boxShadow = "";
                }, 2000);
            }
        });
    }


    // -----------------------------------------
    // 5. Auto-dismiss flash messages after 4s
    // -----------------------------------------
    const flashMessages = document.querySelectorAll(".flash-message");
    flashMessages.forEach(function (msg) {
        setTimeout(function () {
            msg.style.transition = "opacity 0.4s ease, transform 0.4s ease";
            msg.style.opacity = "0";
            msg.style.transform = "translateY(-10px)";
            setTimeout(function () {
                msg.remove();
            }, 400);
        }, 4000);
    });


    // -----------------------------------------
    // 6. Charts (Chart.js) — only on index page
    // -----------------------------------------
    if (typeof chartCategoryLabels !== "undefined" && chartCategoryLabels.length > 0) {
        renderCategoryChart();
    }

    if (typeof chartMonthlyLabels !== "undefined" && chartMonthlyLabels.length > 0) {
        renderMonthlyChart();
    }

});


// ======================================
// CHART RENDERING FUNCTIONS
// ======================================

// Color palette matching our category CSS variables
const categoryColors = {
    "Food": "#f97316",
    "Transport": "#3b82f6",
    "Study": "#22c55e",
    "Entertainment": "#ec4899",
    "Other": "#8b5cf6"
};

const categoryColorsBg = {
    "Food": "rgba(249, 115, 22, 0.7)",
    "Transport": "rgba(59, 130, 246, 0.7)",
    "Study": "rgba(34, 197, 94, 0.7)",
    "Entertainment": "rgba(236, 72, 153, 0.7)",
    "Other": "rgba(139, 92, 246, 0.7)"
};


function renderCategoryChart() {
    const ctx = document.getElementById("category-chart");
    if (!ctx) return;

    const colors = chartCategoryLabels.map(function (label) {
        return categoryColors[label] || "#6c63ff";
    });

    const bgColors = chartCategoryLabels.map(function (label) {
        return categoryColorsBg[label] || "rgba(108, 99, 255, 0.7)";
    });

    new Chart(ctx, {
        type: "doughnut",
        data: {
            labels: chartCategoryLabels,
            datasets: [{
                data: chartCategoryValues,
                backgroundColor: bgColors,
                borderColor: colors,
                borderWidth: 2,
                hoverBorderWidth: 3,
                hoverOffset: 8
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            cutout: "55%",
            plugins: {
                legend: {
                    position: "bottom",
                    labels: {
                        color: "#9898b8",
                        font: {
                            family: "'Inter', sans-serif",
                            size: 11,
                            weight: 500
                        },
                        padding: 16,
                        usePointStyle: true,
                        pointStyleWidth: 10
                    }
                },
                tooltip: {
                    backgroundColor: "#1a1a2e",
                    titleColor: "#e8e8f0",
                    bodyColor: "#9898b8",
                    borderColor: "#2a2a4a",
                    borderWidth: 1,
                    titleFont: { family: "'Inter', sans-serif", weight: 600 },
                    bodyFont: { family: "'Inter', sans-serif" },
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function (context) {
                            const value = context.parsed;
                            const total = context.dataset.data.reduce(function (a, b) { return a + b; }, 0);
                            const pct = ((value / total) * 100).toFixed(1);
                            return ` ₹${value.toFixed(2)} (${pct}%)`;
                        }
                    }
                }
            }
        }
    });
}


function renderMonthlyChart() {
    const ctx = document.getElementById("monthly-chart");
    if (!ctx) return;

    new Chart(ctx, {
        type: "bar",
        data: {
            labels: chartMonthlyLabels,
            datasets: [{
                label: "Monthly Spending (₹)",
                data: chartMonthlyValues,
                backgroundColor: "rgba(108, 99, 255, 0.5)",
                borderColor: "#6c63ff",
                borderWidth: 2,
                borderRadius: 6,
                borderSkipped: false,
                hoverBackgroundColor: "rgba(108, 99, 255, 0.75)"
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            scales: {
                x: {
                    grid: {
                        color: "rgba(42, 42, 74, 0.3)",
                        drawBorder: false
                    },
                    ticks: {
                        color: "#9898b8",
                        font: {
                            family: "'Inter', sans-serif",
                            size: 11
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                    grid: {
                        color: "rgba(42, 42, 74, 0.3)",
                        drawBorder: false
                    },
                    ticks: {
                        color: "#9898b8",
                        font: {
                            family: "'Inter', sans-serif",
                            size: 11
                        },
                        callback: function (value) {
                            return "₹" + value;
                        }
                    }
                }
            },
            plugins: {
                legend: {
                    display: false
                },
                tooltip: {
                    backgroundColor: "#1a1a2e",
                    titleColor: "#e8e8f0",
                    bodyColor: "#9898b8",
                    borderColor: "#2a2a4a",
                    borderWidth: 1,
                    titleFont: { family: "'Inter', sans-serif", weight: 600 },
                    bodyFont: { family: "'Inter', sans-serif" },
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        label: function (context) {
                            return ` ₹${context.parsed.y.toFixed(2)}`;
                        }
                    }
                }
            }
        }
    });
}
