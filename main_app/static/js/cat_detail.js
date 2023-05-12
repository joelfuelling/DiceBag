const dateEl = document.getElementById('id_date');
// M is Materialize's global variable
M.Datepicker.init(dateEl, {
  format: 'yyyy-mm-dd',
  defaultDate: new Date(),
  setDefaultDate: true,
  autoClose: true
});

// add additional JS to initialize select below
const selectEl = document.getElementById('id_result');
M.FormSelect.init(selectEl);