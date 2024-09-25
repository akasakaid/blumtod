import aiofiles
import asyncio
from models import get_all


async def main():
    start_html = """
<!DOCTYPE html>
<html lang="id">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Blum Report</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- DataTables CSS -->
    <link href="https://cdn.datatables.net/1.11.5/css/dataTables.bootstrap5.min.css" rel="stylesheet">
    <style>
        tfoot {
            font-weight: bold;
        }
    </style>
</head>

<body>
    <div class="container mt-5">
        <h1 class="text-center mb-4">Blum Report</h1>
        <div class="table-responsive">
            <table id="dataTable" class="table table-striped table-hover">
                <thead class="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>First Name</th>
                        <th>Balance</th>
                    </tr>
                </thead>
                <tbody>

"""
    end_html = (
        lambda total: """
                </tbody>
                <tfoot class="table-light">
                    <tr>
                        <td colspan="2" class="text-end">Total Balance:</td>
                        <td class="text-end" id="totalBalance">"""
        + str(total)
        + """</td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </div>

    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
    <!-- Bootstrap 5 JS Bundle -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js"></script>
    <!-- DataTables JS -->
    <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.11.5/js/dataTables.bootstrap5.min.js"></script>

    <script>
        $(document).ready(function () {
            // Inisialisasi DataTable
            var table = $('#dataTable').DataTable({
                "pageLength": 10,
                "lengthMenu": [[10, 25, 50, -1], [10, 25, 50, "All"]],
                "language": {
                    "lengthMenu": "Show _MENU_ enteries per page",
                    "zeroRecords": "No matching data",
                    "info": "Show page _PAGE_ from _PAGES_",
                    "infoEmpty": "No data available",
                    "infoFiltered": "(filtered from _MAX_ total entries)",
                    "search": "Search:",
                    "paginate": {
                        "first": "First",
                        "last": "Last",
                        "next": "Next",
                        "previous": "Previous"
                    }
                }
            });
        });
    </script>
</body>

</html>
"""
    )
    tot = 0
    datas = await get_all()
    for i in datas:
        balance = i.get("balance", 0)
        if not balance:
            balance = 0
        tot += float(balance)
        start_html += f"""
<tr>
    <td>{i['id']}</td>
    <td>{i['first_name']}</td>
    <td>{i['balance']}</td>
</tr>"""
    print(f"Total account : {len(datas)}")
    print(f"Total blum point : {int(tot)}")
    async with aiofiles.open("report.html", "w", encoding="utf-8") as w:
        await w.write(start_html + end_html(tot))
    print(f"See html/web report open report.html")


asyncio.run(main())
