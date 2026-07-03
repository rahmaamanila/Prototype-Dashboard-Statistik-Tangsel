from django.core.management.base import BaseCommand

from dashboard.services.sosial import (
    sync_semua_data_sosial,
)

from dashboard.services.ekonomi import (
    sync_semua_data_ekonomi,
)

from dashboard.services.sosial_tambahan import (
    sync_semua_data_tambahan,
)


class Command(BaseCommand):

    help = "Sinkronisasi seluruh dataset Portal Data Tangsel"

    def handle(self, *args, **kwargs):

        self.stdout.write("")
        self.stdout.write("=" * 70)
        self.stdout.write(
            "        SINKRONISASI DASHBOARD STATISTIK TANGSEL"
        )
        self.stdout.write("=" * 70)

        # ==================================================
        # DATASET SOSIAL
        # ==================================================

        sync_semua_data_sosial()

        # ==================================================
        # DATASET EKONOMI
        # ==================================================

        sync_semua_data_ekonomi()

        # ==================================================
        # DATASET TAMBAHAN
        # ==================================================

        sync_semua_data_tambahan()

        self.stdout.write("")
        self.stdout.write(
            self.style.SUCCESS(
                "✓ Sinkronisasi seluruh dataset berhasil."
            )
        )