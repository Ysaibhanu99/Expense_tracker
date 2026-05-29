// ======================================
// EXPENSE TRACKER — CLIENT-SIDE SCRIPT
// ======================================

document.addEventListener("DOMContentLoaded", function () {

    // 1. Auto-set today's date in the date input
    const dateInput = document.getElementById("date");
    if (dateInput && !dateInput.value) {
        const today = new Date();
        const yyyy = today.getFullYear();
        const mm = String(today.getMonth() + 1).padStart(2, "0");
        const dd = String(today.getDate()).padStart(2, "0");
        dateInput.value = `${yyyy}-${mm}-${dd}`;
    }


    // 2. Delete confirmation
    const deleteForms = document.querySelectorAll(".delete-form");
    deleteForms.forEach(function (form) {
        form.addEventListener("submit", function (e) {
            const confirmed = confirm("Are you sure you want to delete this expense?");
            if (!confirmed) {
                e.preventDefault();
            }
        });
    });


    // 3. Basic form validation — prevent amount <= 0
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

                // Reset after 2 seconds
                setTimeout(function () {
                    amountInput.style.borderColor = "";
                    amountInput.style.boxShadow = "";
                }, 2000);
            }
        });
    }

});
