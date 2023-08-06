$(function() {
  // $('.datatables-demo').dataTable();

  $('.datatables-demo').DataTable( {
    // dom: 'Blfrtip',
    buttons: [
        'copyHtml5',
        'excelHtml5',
        'csvHtml5',
        'pdfHtml5'
    ]
} );
});
